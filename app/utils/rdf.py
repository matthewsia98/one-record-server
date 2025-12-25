from typing import Optional

from rdflib.util import FORMAT_MIMETYPE_MAP


def get_format_from_mime_type(mime_type: str) -> Optional[str]:
    for short, long in FORMAT_MIMETYPE_MAP.items():
        if long[0] in mime_type:
            return short
    return None
