import json
from datetime import datetime, date

from pydantic import HttpUrl


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, HttpUrl):
            return str(obj)
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)