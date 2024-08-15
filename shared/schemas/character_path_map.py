from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.map import CoordinatesMapSchema, MapSchema


class BaseCharacterPathMapSchema(BaseSchemaOrm):
    order_index: int
    character_path_info_id: int


class ReadCharacterPathMapSchema(BaseCharacterPathMapSchema):
    id: int
    map_id: int
    map: MapSchema


class CreateUpdateCharacterPathMapSchema(BaseCharacterPathMapSchema):
    map: CoordinatesMapSchema
