from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.item import ItemSchema


class IngredientSchema(BaseSchemaOrm):
    id: int
    item_id: int
    item: ItemSchema
    quantity: int
    recipe_id: int

    def __hash__(self) -> int:
        return self.id.__hash__()
