from typing import Any

from shared.schemas.base import BaseSchemaOrm
from shared.schemas.world import WorldSchema


class BaseMapSchema(BaseSchemaOrm):
    id: int
    x: int
    y: int
    world_id: int = 1

    sub_area_id: int

    allow_teleport_from: bool
    allow_monster_fight: bool
    has_priority_on_world_map: bool

    def __hash__(self) -> int:
        return self.id.__hash__()

    def __eq__(self, value: Any) -> bool:
        return isinstance(value, BaseMapSchema) and self.id == value.id

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


from shared.schemas.sub_area import SubAreaSchema
from shared.schemas.waypoint import WaypointSchema

MapSchema.model_rebuild()
