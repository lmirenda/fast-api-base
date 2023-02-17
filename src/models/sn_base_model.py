from datetime import datetime

from pydantic import BaseModel


class SNBaseModel(BaseModel):
    class Config:
        json_encoders = {
            datetime: lambda v: v.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        anystr_strip_whitespace = True
        arbitrary_types_allowed = True
        underscore_attrs_are_private = True

    def dict(self, *args, **kwargs):
        kwargs["exclude_none"] = True
        return super().dict(*args, **kwargs)
