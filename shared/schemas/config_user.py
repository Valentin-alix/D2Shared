from datetime import time

from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.range_time import (
    ReadRangeWaitSchema,
    UpdateRangeWaitSchema,
)


class BaseConfigUserSchema(BaseSchemaOrm):
    time_between_sentence: time
    time_fighter: time
    time_harvester: time


class ReadConfigUserSchema(BaseConfigUserSchema):
    id: int

    range_new_map_id: int
    range_new_map: ReadRangeWaitSchema

    user_id: int


class UpdateConfigUserSchema(BaseConfigUserSchema):
    range_new_map: UpdateRangeWaitSchema
