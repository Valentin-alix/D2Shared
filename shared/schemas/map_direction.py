from shared.enums import FromDirection, ToDirection
from shared.schemas.base import BaseSchemaOrm
from shared.schemas.map import MapSchema


class MapDirectionSchema(BaseSchemaOrm):
    id: int
    from_map_id: int
    from_direction: FromDirection

    to_map_id: int
    to_map: MapSchema
    to_direction: ToDirection
    was_checked: bool

    def __hash__(self) -> int:
        return self.id.__hash__()
