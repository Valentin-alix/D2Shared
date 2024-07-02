from datetime import time

from D2Shared.shared.schemas.base import BaseSchemaOrm


class RangeHourPlayTimeSchema(BaseSchemaOrm):
    id: int
    start_time: time
    end_time: time
    config_user_id: int


class RangeTimeSchema(BaseSchemaOrm):
    id: int
    start_time: time
    end_time: time


class ConfigUserSchema(BaseSchemaOrm):
    id: int
    ranges_hour_playtime: list[RangeHourPlayTimeSchema]
    afk_time_at_start: time | None
    time_between_sentence: time
    time_fighter: time
    time_harvester: time
    randomizer_duration_activity: float

    range_new_map_id: int
    range_new_map: RangeTimeSchema

    range_wait_id: int
    range_wait: RangeTimeSchema

    user_id: int
