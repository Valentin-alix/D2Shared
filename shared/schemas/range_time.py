from D2Shared.shared.schemas.base import BaseSchemaOrm


from datetime import time


class BaseRangeHourPlayTimeSchema(BaseSchemaOrm):
    start_time: time
    end_time: time


class ReadRangeHourPlayTimeSchema(BaseRangeHourPlayTimeSchema):
    id: int
    config_user_id: int


class UpdateRangeHourPlayTimeSchema(BaseRangeHourPlayTimeSchema): ...


class BaseRangeTimeSchema(BaseSchemaOrm):
    start_time: time
    end_time: time


class ReadRangeTimeSchema(BaseRangeTimeSchema):
    id: int


class UpdateRangeTimeSchema(BaseRangeTimeSchema): ...
