import re
import subprocess
from io import StringIO

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
browser = webdriver.Chrome(options=options)
browser.get("https://onerecord.iata.org/ns/code-lists/index-en.html")

# Wait until the first <table> element is present (max 10 seconds)
wait = WebDriverWait(browser, 10)
table_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))

tables = pd.read_html(StringIO(browser.page_source))
df = tables[0]

_CODE = '''\
from rdflib.namespace import DefinedNamespace, Namespace


class CODE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-25 01:04:52.379792
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/")
'''

for index, row in df.iterrows():
    object_id = row[0].upper()
    target_namespace = row[1].strip("<>")
    if re.match(r"https://onerecord.iata.org/ns/code-lists/\w+#", target_namespace):
        subprocess.run(
            [
                "uv",
                "run",
                "python",
                "-m",
                "rdflib.tools.defined_namespace_creator",
                "https://onerecord.iata.org/ns/code-lists/ontology.ttl",
                target_namespace,
                object_id,
            ]
        )

browser.quit()
