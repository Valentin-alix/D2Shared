from pydantic import BaseModel

from D2Shared.shared.consts.adaptative.consts import SPELL_CELL_SIZE
from D2Shared.shared.consts.adaptative.positions import (
    EMPTY_POSITION,
    FIRST_SPELL_BAR_POSITION,
)
from D2Shared.shared.entities.position import Position
from D2Shared.shared.enums import CharacteristicEnum, ElemEnum
from D2Shared.shared.schemas.base import BaseSchemaOrm


class SpellSchema(BaseSchemaOrm):
    id: int
    name: str
    character_id: int
    index: int
    elem: ElemEnum
    is_disenchantment: bool
    boost_char: CharacteristicEnum
    is_healing: bool
    is_for_enemy: bool
    ap_cost: int
    max_cast: int
    min_range: int
    range: int
    duration_boost: int
    boostable_range: bool
    level: int

    def __hash__(self) -> int:
        return self.id.__hash__()

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


class CurrentBoostSchema(BaseModel):
    spell_level_id: int
    expire_turn: int

    def __hash__(self) -> int:
        return self.spell_level_id.__hash__()
