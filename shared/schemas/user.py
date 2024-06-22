from datetime import datetime
from EzreD2Shared.shared.schemas.base import BaseSchemaOrm


class BaseUserSchema(BaseSchemaOrm):
    email: str


class ReadUserSchema(BaseUserSchema):
    sub_expire: datetime


class CreateUserSchema(BaseUserSchema):
    password: str
