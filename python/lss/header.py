from enum import Enum
from typing import Dict

class ContentType(Enum):
    NONE = 0
    JSON = 1

    @staticmethod
    def json_header() -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    @staticmethod
    def none_header() -> Dict[str, str]:
        return {}

def create_header(content_type: ContentType) -> Dict[str, str]:
    types = {
        ContentType.NONE: ContentType.none_header(),
        ContentType.JSON: ContentType.json_header()
    }
    return types.get(content_type)