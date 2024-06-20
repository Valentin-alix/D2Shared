from pydantic import BaseModel
from shared.enums import FromDirection


from typing import Any

from shared.schemas.map import MapSchema
from shared.schemas.map_direction import MapDirectionSchema
from shared.schemas.waypoint import WaypointSchema
from shared.schemas.zaapi import ZaapiSchema

type ActionMapChangeSchema = MapDirectionSchema | ZaapiSchema | WaypointSchema


class MapWithActionSchema(BaseModel):
    map: MapSchema
    current_direction: FromDirection
    from_action: ActionMapChangeSchema | None = None

    def __eq__(self, value: Any) -> bool:
        return (
            isinstance(value, MapWithActionSchema)
            and self.map.id == value.map.id
            and self.current_direction == value.current_direction
        )

    def __str__(self) -> str:
        return f"{self.from_action} to {self.map}:{self.current_direction}"

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return (self.map.id, self.current_direction).__hash__()
