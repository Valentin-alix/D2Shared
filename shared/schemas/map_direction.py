from D2Shared.shared.enums import ToDirection
from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.map import MapSchema


class MapDirectionSchema(BaseSchemaOrm):
    id: int

    from_map_id: int
    from_map: MapSchema

    to_map_id: int
    to_map: MapSchema

    was_checked: bool
    direction: ToDirection
