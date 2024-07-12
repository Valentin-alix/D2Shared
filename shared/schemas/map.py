from typing import Any

from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.world import WorldSchema


class CoordinatesMapSchema(BaseSchemaOrm):
    x: int
    y: int
    world_id: int = 1


class BaseMapSchema(CoordinatesMapSchema):
    id: int
    x: int
    y: int
    world_id: int = 1

    sub_area_id: int
    sub_area: "SubAreaSchema"

    allow_teleport_from: bool
    allow_monster_fight: bool
    has_priority_on_world_map: bool

    def __hash__(self) -> int:
        return self.id.__hash__()

    def __eq__(self, value: Any) -> bool:
        return isinstance(value, BaseMapSchema) and self.id == value.id

    def __str__(self) -> str:
        return (
            f"x:{self.x} y:{self.y} monde:{self.world_id} sous zone:{self.sub_area_id}."
        )

    def get_dist_map(self, map: "BaseMapSchema") -> float:
        # Manhattan distance
        if self.world_id != map.world_id:
            return float("inf")
        return abs(self.x - map.x) + abs(self.y - map.y)


class MapSchema(BaseMapSchema):
    world: WorldSchema
    sub_area: "SubAreaSchema"

    # map_directions: list["MapDirectionSchema"]

    waypoint: "WaypointSchema | None"
    # collectables_map_info: list[CollectableMapInfoSchema]


from D2Shared.shared.schemas.sub_area import SubAreaSchema
from D2Shared.shared.schemas.waypoint import WaypointSchema

MapSchema.model_rebuild()
