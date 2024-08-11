from typing import Any

from pydantic import BaseModel

from D2Shared.shared.enums import ToDirection
from D2Shared.shared.schemas.map import MapSchema
from D2Shared.shared.schemas.waypoint import WaypointSchema
from D2Shared.shared.schemas.zaapi import ZaapiSchema


class MapDirectionSchema(BaseModel):
    direction: ToDirection
    map: MapSchema


type ActionMapChangeSchema = MapDirectionSchema | ZaapiSchema | WaypointSchema


class MapWithActionSchema(BaseModel):
    map_id: int
    from_action: ActionMapChangeSchema | None = None

    def __eq__(self, value: Any) -> bool:
        return isinstance(value, MapWithActionSchema) and self.map_id == value.map_id

    def __str__(self) -> str:
        return f"{self.from_action.__class__.__name__} -> {self.from_action}"

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return self.map_id.__hash__()
