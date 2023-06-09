# Python
from typing import Optional
from uuid import uuid4
import re

# Pydantic
from pydantic import BaseModel, validator
from pydantic import Extra
from pydantic import Field
from pydantic import EmailStr


class Inbox(BaseModel):
    id: Optional[str] = uuid4()
    name: str
    email: EmailStr
    number_phone: str

    @validator('number_phone')
    def validate_number_phone(cls, value):
        if not re.match(r'^\d{3}\d{7}$', value):
            raise ValueError('number_phone must be in the format "XXX-XXXXXXX"')
        return value
    
    class Config:
        extra = Extra.forbid

inbox_schema = Inbox.schema()