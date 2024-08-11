from typing import Any


from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.map_direction import MapDirectionSchema
from D2Shared.shared.schemas.waypoint import WaypointSchema
from D2Shared.shared.schemas.zaapi import ZaapiSchema


type ActionMapChangeSchema = MapDirectionSchema | ZaapiSchema | WaypointSchema


class MapWithActionSchema(BaseSchemaOrm):
    map_id: int
    from_action: ActionMapChangeSchema | None = None

    def __eq__(self, value: Any) -> bool:
        return isinstance(value, MapWithActionSchema) and self.map_id == value.map_id

    def __str__(self) -> str:
        return str(self.from_action)

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return self.map_id.__hash__()
