from datetime import time

from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.range_time import (
    ReadRangeHourPlayTimeSchema,
    ReadRangeTimeSchema,
    UpdateRangeHourPlayTimeSchema,
    UpdateRangeTimeSchema,
)


class BaseConfigUserSchema(BaseSchemaOrm):
    afk_time_at_start: time | None
    time_between_sentence: time
    time_fighter: time
    time_harvester: time
    randomizer_duration_activity: float


class ReadConfigUserSchema(BaseConfigUserSchema):
    id: int
    ranges_hour_playtime: list[ReadRangeHourPlayTimeSchema]

    range_new_map_id: int
    range_new_map: ReadRangeTimeSchema

    range_wait_id: int
    range_wait: ReadRangeTimeSchema

    user_id: int


class UpdateConfigUserSchema(BaseConfigUserSchema):
    ranges_hour_playtime: list[UpdateRangeHourPlayTimeSchema]
    range_new_map: UpdateRangeTimeSchema
    range_wait: UpdateRangeTimeSchema
