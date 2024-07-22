from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.ingredient import IngredientSchema
from D2Shared.shared.schemas.item import ItemSchema
from D2Shared.shared.schemas.job import JobSchema


class RecipeSchema(BaseSchemaOrm):
    id: int
    result_item_id: int
    result_item: ItemSchema
    ingredients: list[IngredientSchema]
    job_id: int
    job: JobSchema

    receipe_pod_cost: int

    def __eq__(self, value: object) -> bool:
        return isinstance(value, RecipeSchema) and self.id == value.id

    def __hash__(self) -> int:
        return self.id.__hash__()

    def __str__(self) -> str:
        return self.result_item.name

    def __repr__(self) -> str:
        return self.__str__()
