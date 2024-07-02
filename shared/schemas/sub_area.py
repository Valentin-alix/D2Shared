from D2Shared.shared.schemas.area import AreaSchema
from D2Shared.shared.schemas.base import BaseSchemaOrm


class SubAreaSchema(BaseSchemaOrm):
    id: int
    name: str
    area_id: int
    area: AreaSchema
    # maps: list[MapSchema]
    level: int
    # monsters: list[MonsterSchema]

    def __hash__(self) -> int:
        return self.id.__hash__()
