from datetime import time

from D2Shared.shared.schemas.base import BaseSchemaOrm


class BaseRangeHourPlayTimeSchema(BaseSchemaOrm):
    start_time: time
    end_time: time


class ReadRangeHourPlayTimeSchema(BaseRangeHourPlayTimeSchema):
    id: int
    config_user_id: int


class UpdateRangeHourPlayTimeSchema(BaseRangeHourPlayTimeSchema): ...


class BaseRangeWaitSchema(BaseSchemaOrm):
    start: float
    end: float


class ReadRangeWaitSchema(BaseRangeWaitSchema):
    id: int


class UpdateRangeWaitSchema(BaseRangeWaitSchema): ...
