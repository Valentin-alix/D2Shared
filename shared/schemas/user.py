from datetime import datetime
from D2Shared.shared.schemas.base import BaseSchemaOrm
from pydantic import EmailStr

from D2Shared.shared.schemas.config_user import ReadConfigUserSchema


class BaseUserSchema(BaseSchemaOrm):
    email: EmailStr


class ReadUserSchema(BaseUserSchema):
    sub_expire: datetime
    config_user: ReadConfigUserSchema


class CreateUserSchema(BaseUserSchema):
    password: str
