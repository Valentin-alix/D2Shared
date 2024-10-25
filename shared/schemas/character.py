from typing import Annotated

from pydantic import conint

from D2Shared.shared.enums import ElemEnum
from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.character_job_info import CharacterJobInfoSchema
from D2Shared.shared.schemas.character_path_info import ReadCharacterPathInfoSchema
from D2Shared.shared.schemas.item import ItemSchema, SellItemInfo
from D2Shared.shared.schemas.recipe import RecipeSchema
from D2Shared.shared.schemas.spell import SpellSchema
from D2Shared.shared.schemas.sub_area import SubAreaSchema
from D2Shared.shared.schemas.waypoint import WaypointSchema


class BaseCharacterSchema(BaseSchemaOrm):
    id: str
    lvl: Annotated[int, conint(ge=1, le=200)] = 1
    po_bonus: int = 0
    elem: ElemEnum = ElemEnum.ELEMENT_WATER
    server_id: int


class UpdateCharacterSchema(BaseCharacterSchema): ...


class CharacterSchema(BaseCharacterSchema):
    jobs_infos: list[CharacterJobInfoSchema]
    max_pods: int
    waypoints: list[WaypointSchema]
    sub_areas: list[SubAreaSchema]
    spells: list[SpellSchema]
    recipes: list[RecipeSchema]
    sell_items_infos: list[SellItemInfo]
    bank_items: list[ItemSchema]
    paths_infos: list[ReadCharacterPathInfoSchema]

    def __eq__(self, value: object) -> bool:
        return isinstance(value, CharacterSchema) and value.id == self.id

    def __hash__(self) -> int:
        return self.id.__hash__()

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return self.__str__()
