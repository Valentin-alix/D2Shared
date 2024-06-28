from pydantic import BaseModel

from EzreD2Shared.shared.consts.adaptative.consts import SPELL_CELL_SIZE
from EzreD2Shared.shared.consts.adaptative.positions import (
    EMPTY_POSITION,
    FIRST_SPELL_BAR_POSITION,
)
from EzreD2Shared.shared.entities.position import Position
from EzreD2Shared.shared.enums import DispellableEnum
from EzreD2Shared.shared.schemas.base import BaseSchemaOrm
from EzreD2Shared.shared.schemas.breed import BreedSchema
from EzreD2Shared.shared.schemas.effect import EffectSchema


class SpellVariantSchema(BaseSchemaOrm):
    id: int
    breed_id: int
    breed: BreedSchema
    spells: list["SpellSchema"]

    def __hash__(self) -> int:
        return self.id.__hash__()


class SpellSchema(BaseSchemaOrm):
    id: int
    name: str
    spell_variant_id: int
    default_index: int

    def __hash__(self) -> int:
        return self.id.__hash__()


class SpellLevelEffect(BaseSchemaOrm):
    id: int
    spell_level_id: int
    spell_level: "SpellLevelSchema"
    effect_id: int
    effect: EffectSchema
    duration: int
    dispellable: DispellableEnum

    def __hash__(self) -> int:
        return self.id.__hash__()


class SpellLevelSchema(BaseSchemaOrm):
    id: int
    spell_id: int
    spell: SpellSchema
    ap_cost: int
    max_cast: int
    min_range: int
    range: int
    can_cast_in_line: bool
    can_cast_in_diagonal: bool
    need_los: bool

    is_disenchantment: bool
    is_boost: bool
    is_healing: bool
    on_enemy: bool
    duration_boost: int

    need_free_cell: bool
    need_taken_cell: bool
    need_visible_entity: bool
    range_can_be_boosted: bool
    max_stack: int
    min_cast_interval: int
    initial_cooldown: int
    global_cooldown: int
    min_player_level: int

    def __hash__(self) -> int:
        return self.id.__hash__()

    def __str__(self) -> str:
        return self.spell.name

    def get_pos_spell(self) -> Position:
        line_brut = (self.spell.default_index + 10) // 10
        col = self.spell.default_index % 10

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
