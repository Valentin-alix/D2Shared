from typing import Any

from pydantic import BaseModel

from D2Shared.shared.enums import FromDirection
from D2Shared.shared.schemas.map_direction import MapDirectionSchema
from D2Shared.shared.schemas.waypoint import WaypointSchema
from D2Shared.shared.schemas.zaapi import ZaapiSchema

type ActionMapChangeSchema = MapDirectionSchema | ZaapiSchema | WaypointSchema


class MapWithActionSchema(BaseModel):
    map_id: int
    current_direction: FromDirection
    from_action: ActionMapChangeSchema | None = None

    def __eq__(self, value: Any) -> bool:
        return (
            isinstance(value, MapWithActionSchema)
            and self.map_id == value.map_id
            and self.current_direction == value.current_direction
        )

    def __str__(self) -> str:
        return f"{self.from_action.__class__.__name__} -> {self.from_action}"

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return (self.map_id, self.current_direction).__hash__()
