from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.stat import LineSchema


class BaseEquipmentSchema(BaseSchemaOrm):
    label: str
    lines: list[LineSchema]


class ReadEquipmentSchema(BaseEquipmentSchema):
    id: int


class UpdateEquipmentSchema(BaseEquipmentSchema): ...
