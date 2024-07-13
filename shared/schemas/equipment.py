from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.stat import BaseLineSchema, LineSchema


class BaseEquipmentSchema(BaseSchemaOrm):
    label: str


class ReadEquipmentSchema(BaseEquipmentSchema):
    id: int
    lines: list[LineSchema]
    exo_line: LineSchema | None
    count_attempt: int

    def __eq__(self, value: object) -> bool:
        return isinstance(value, ReadEquipmentSchema) and self.id == value.id

    def __hash__(self) -> int:
        return self.id.__hash__()


class UpdateEquipmentSchema(BaseEquipmentSchema):
    lines: list[BaseLineSchema]
    exo_line: BaseLineSchema | None
