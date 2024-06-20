from __future__ import annotations

from shared.schemas.base import BaseSchemaOrm


class WaypointSchema(BaseSchemaOrm):
    id: int
    map_id: int
    map: "BaseMapSchema"

    def __hash__(self) -> int:
        return self.id.__hash__()


from shared.schemas.map import BaseMapSchema

WaypointSchema.model_rebuild()
