from datetime import time

from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.range_time import (
    ReadRangeHourPlayTimeSchema,
    ReadRangeWaitSchema,
    UpdateRangeHourPlayTimeSchema,
    UpdateRangeWaitSchema,
)


class BaseConfigUserSchema(BaseSchemaOrm):
    time_between_sentence: time
    time_fighter: time
    time_harvester: time


class ReadConfigUserSchema(BaseConfigUserSchema):
    id: int
    ranges_hour_playtime: list[ReadRangeHourPlayTimeSchema]

    range_new_map_id: int
    range_new_map: ReadRangeWaitSchema

    user_id: int


class UpdateConfigUserSchema(BaseConfigUserSchema):
    ranges_hour_playtime: list[UpdateRangeHourPlayTimeSchema]
    range_new_map: UpdateRangeWaitSchema
