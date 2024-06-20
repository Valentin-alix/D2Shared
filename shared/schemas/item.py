from shared.schemas.base import BaseSchemaOrm
from shared.schemas.type_item import TypeItemSchema


class ItemSchema(BaseSchemaOrm):
    id: int
    name: str
    type_item_id: int
    type_item: TypeItemSchema
    level: int
    weight: int
    # recipe: "RecipeSchema"
    icon_id: int | None = None
    is_saleable: bool

    def __hash__(self) -> int:
        return self.id.__hash__()


ItemSchema.model_rebuild()
