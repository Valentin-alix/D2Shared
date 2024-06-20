from shared.schemas.base import BaseSchemaOrm


class CharacteristicCategorySchema(BaseSchemaOrm):
    id: int
    name: str

    def __hash__(self) -> int:
        return self.id.__hash__()


class CharacteristicSchema(BaseSchemaOrm):
    id: int
    name: str
    characteristic_category_id: int
    characteristic_category: CharacteristicCategorySchema | None

    def __hash__(self) -> int:
        return self.id.__hash__()
