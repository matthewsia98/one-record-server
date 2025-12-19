from datetime import datetime
from typing import Optional

from fastapi import Query


def parse_datetime_param(
    param_name: str,
    description: Optional[str] = None,
) -> datetime:
    def wrapper(
        value: str = Query(
            default=None,
            alias=param_name,
            description=description,
            example="20190926T075830Z",
        ),
    ):
        if value is None:
            return None

        return datetime.fromisoformat(value)

    return wrapper
