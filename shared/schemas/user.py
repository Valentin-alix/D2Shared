from datetime import datetime
from EzreD2Shared.shared.schemas.base import BaseSchemaOrm
from pydantic import EmailStr


class BaseUserSchema(BaseSchemaOrm):
    email: EmailStr


class ReadUserSchema(BaseUserSchema):
    sub_expire: datetime


class CreateUserSchema(BaseUserSchema):
    password: str
