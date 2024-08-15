from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.character_path_map import ReadCharacterPathMapSchema


class BaseCharacterPathInfoSchema(BaseSchemaOrm):
    name: str


class ReadCharacterPathInfoSchema(BaseCharacterPathInfoSchema):
    id: int
    character_id: str
    path_maps: list[ReadCharacterPathMapSchema]


class UpdateCharacterPathInfoSchema(BaseCharacterPathInfoSchema): ...


class CreateCharacterPathInfoSchema(BaseCharacterPathInfoSchema):
    character_id: str
