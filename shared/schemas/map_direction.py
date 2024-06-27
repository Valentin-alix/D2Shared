from EzreD2Shared.shared.enums import FromDirection, ToDirection
from EzreD2Shared.shared.schemas.base import BaseSchemaOrm


class MapDirectionSchema(BaseSchemaOrm):
    id: int
    from_map_id: int
    from_direction: FromDirection

    to_map_id: int
    to_direction: ToDirection
    was_checked: bool

    def __hash__(self) -> int:
        return self.id.__hash__()
