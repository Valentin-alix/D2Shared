from typing import Annotated

from pydantic import PositiveInt, conint

from D2Shared.shared.enums import ElemEnum
from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.job import JobSchema
from D2Shared.shared.schemas.recipe import RecipeSchema
from D2Shared.shared.schemas.spell import SpellSchema
from D2Shared.shared.schemas.sub_area import SubAreaSchema
from D2Shared.shared.schemas.waypoint import WaypointSchema


class CharacterJobInfoSchema(BaseSchemaOrm):
    character_id: str
    job_id: PositiveInt
    job: JobSchema
    lvl: Annotated[int, conint(ge=1, le=200)]
    weight: float

    def __hash__(self) -> int:
        return (self.character_id, self.job_id).__hash__()


class BaseCharacterSchema(BaseSchemaOrm):
    id: str
    lvl: Annotated[int, conint(ge=1, le=200)] = 1
    po_bonus: int = 0
    is_sub: bool = True
    time_spent: float = 0
    elem: ElemEnum = ElemEnum.ELEMENT_WATER
    server_id: PositiveInt


class UpdateCharacterSchema(BaseCharacterSchema): ...


class CharacterSchema(BaseCharacterSchema):
    character_job_info: list[CharacterJobInfoSchema]
    max_pods: int
    waypoints: list[WaypointSchema]
    sub_areas: list[SubAreaSchema]
    spells: list[SpellSchema]
    recipes: list[RecipeSchema]

    def __eq__(self, value: object) -> bool:
        return isinstance(value, CharacterSchema) and value.id == self.id

    def __hash__(self) -> int:
        return self.id.__hash__()

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return self.__str__()
