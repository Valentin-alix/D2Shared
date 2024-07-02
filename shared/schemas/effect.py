from D2Shared.shared.enums import ElemEnum
from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.characteristic import CharacteristicSchema


class EffectSchema(BaseSchemaOrm):
    id: int
    is_boost: bool
    characteristic_id: int
    characteristic: CharacteristicSchema
    description: str
    operator: str
    elem: ElemEnum
    use_in_fight: bool

    def __hash__(self) -> int:
        return self.id.__hash__()
