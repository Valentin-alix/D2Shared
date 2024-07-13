from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.stat import LineSchema


class BaseEquipmentSchema(BaseSchemaOrm):
    label: str
    lines: list[LineSchema]


class ReadEquipmentSchema(BaseEquipmentSchema):
    id: int
    count_attempt: int

    def __eq__(self, value: object) -> bool:
        return isinstance(value, ReadEquipmentSchema) and self.id == value.id

    def __hash__(self) -> int:
        return self.id.__hash__()


class UpdateEquipmentSchema(BaseEquipmentSchema): ...
