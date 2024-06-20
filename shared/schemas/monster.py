from shared.schemas.base import BaseSchemaOrm
from shared.schemas.drop import DropSchema


class MonsterSchema(BaseSchemaOrm):
    id: int
    name: str
    earth_resistance: int
    air_resistance: int
    fire_resistance: int
    water_resistance: int
    # sub_areas: list[SubAreaSchema]
    drops: list[DropSchema]

    def __hash__(self) -> int:
        return self.id.__hash__()
