import json

from pydantic import HttpUrl


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, HttpUrl):
            return str(obj)  # Convert HttpUrl to string
        return json.JSONEncoder.default(self, obj)
