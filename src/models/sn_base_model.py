from pydantic import BaseModel
from datetime import datetime


class SNBaseModel(BaseModel):
    class Config:
        # enable JSON encoding/decoding
        json_encoders = {
            datetime: lambda v: v.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        # Whether to strip leading and trailing whitespace for str & byte types
        anystr_strip_whitespace = True
        # support classes that are not pydantic models
        arbitrary_types_allowed = True
        # make all underscore attrs are private
        underscore_attrs_are_private = True

    def dict(self, *args, **kwargs):
        kwargs["exclude_none"] = True
        return super().dict(*args, **kwargs)
