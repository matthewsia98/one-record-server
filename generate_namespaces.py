import datetime
import os
import re
import subprocess
from io import StringIO
from pathlib import Path
from tempfile import NamedTemporaryFile

import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Path("app/namespaces").mkdir(parents=True, exist_ok=True)


subprocess.run(
    [
        "uv",
        "run",
        "python",
        "-m",
        "rdflib.tools.defined_namespace_creator",
        "--fail",
        "https://onerecord.iata.org/ns/api/ontology.ttl",
        "https://onerecord.iata.org/ns/api#",
        "API",
    ],
    check=True,
    env={**os.environ, "PYTHONUTF8": "1"},
)
Path("_API.py").replace("app/namespaces/_API.py")

subprocess.run(
    [
        "uv",
        "run",
        "python",
        "-m",
        "rdflib.tools.defined_namespace_creator",
        "--fail",
        "https://onerecord.iata.org/ns/cargo/ontology.ttl",
        "https://onerecord.iata.org/ns/cargo#",
        "CARGO",
    ],
    check=True,
    env={**os.environ, "PYTHONUTF8": "1"},
)
Path("_CARGO.py").replace("app/namespaces/_CARGO.py")


options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
browser = webdriver.Chrome(options=options)
browser.get("https://onerecord.iata.org/ns/code-lists/index-en.html")

# Wait until the first <table> element is present (max 10 seconds)
wait = WebDriverWait(browser, 10)
table_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))

tables = pd.read_html(StringIO(browser.page_source))
df = tables[0]

browser.quit()


Path("app/namespaces/code_lists").mkdir(parents=True, exist_ok=True)


response = requests.get("https://onerecord.iata.org/ns/code-lists/ontology.ttl")
with NamedTemporaryFile(mode="wb", suffix=".ttl", delete=False) as tmp_file:
    tmp_file.write(response.content)
    code_lists_ontology_file = tmp_file.name


object_ids = []
for index, row in df.iterrows():
    original_object_id = str(row[0])
    object_id = str(row[0]).upper()
    target_namespace = str(row[1]).strip("<>")

    if re.match(r"https://onerecord.iata.org/ns/code-lists/\w+#", target_namespace):
        object_ids.append((original_object_id, object_id))

        subprocess.run(
            [
                "uv",
                "run",
                "python",
                "-m",
                "rdflib.tools.defined_namespace_creator",
                "--fail",
                code_lists_ontology_file,
                target_namespace,
                object_id,
            ],
            check=True,
            env={"PYTHONUTF8": "1"},
        )

        Path(f"_{object_id}.py").replace(f"app/namespaces/code_lists/_{object_id}.py")


_CODELISTS = f'''\
from rdflib.namespace import DefinedNamespace, Namespace
{"\n".join([f"from app.namespaces.code_lists._{object_id} import {object_id}" for _, object_id in object_ids])}


class CODELISTS(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: {datetime.datetime.now(tz=datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f")}
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/")

    {"\n    ".join([f"{original_object_id}: type[DefinedNamespace] = {object_id}" for original_object_id, object_id in object_ids])}
'''
with open("app/namespaces/_CODELISTS.py", "w") as f:
    f.write(_CODELISTS)


__INIT__ = """\
from app.namespaces._API import API
from app.namespaces._CARGO import CARGO
from app.namespaces._CODELISTS import CODELISTS


__all__ = [
    API.__name__,
    CARGO.__name__,
    CODELISTS.__name__,
]
"""
with open("app/namespaces/__init__.py", "w") as f:
    f.write(__INIT__)


subprocess.run(
    ["uvx", "ruff", "check", "--fix", "app/namespaces"],
    check=True,
)
subprocess.run(
    ["uvx", "ruff", "format", "app/namespaces"],
    check=True,
)
