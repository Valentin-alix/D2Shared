from pydantic import BaseModel

from D2Shared.shared.consts.adaptative.consts import SPELL_CELL_SIZE
from D2Shared.shared.consts.adaptative.positions import (
    EMPTY_POSITION,
    FIRST_SPELL_BAR_POSITION,
)
from D2Shared.shared.entities.position import Position
from D2Shared.shared.enums import CharacteristicEnum, ElemEnum
from D2Shared.shared.schemas.base import BaseSchemaOrm


class BaseSpellSchema(BaseSchemaOrm):
    name: str
    character_id: str
    index: int
    elem: ElemEnum
    is_disenchantment: bool
    boost_char: CharacteristicEnum | None
    is_healing: bool
    is_for_enemy: bool
    ap_cost: int
    max_cast: int
    min_range: int
    range: int
    duration_boost: int
    boostable_range: bool
    level: int

    def get_pos_spell(self) -> Position:
        line_brut = (self.index + 10) // 10
        col = self.index % 10

        num_page = line_brut // 2
        if line_brut % 2 == 1:
            num_page += 1
            line = 0
        else:
            line = 1

        if num_page >= 2:
            return EMPTY_POSITION

        return Position(
            x_pos=FIRST_SPELL_BAR_POSITION.x_pos + SPELL_CELL_SIZE * (col),
            y_pos=FIRST_SPELL_BAR_POSITION.y_pos + SPELL_CELL_SIZE * (line),
        )


class UpdateSpellSchema(BaseSpellSchema): ...


class SpellSchema(BaseSpellSchema):
    id: int

    def __hash__(self) -> int:
        return self.id.__hash__()


class CurrentBoostSchema(BaseModel):
    spell_level_id: int
    expire_turn: int

    def __hash__(self) -> int:
        return self.spell_level_id.__hash__()
