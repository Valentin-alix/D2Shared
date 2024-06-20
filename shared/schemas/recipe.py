from shared.schemas.base import BaseSchemaOrm
from shared.schemas.item import ItemSchema
from shared.schemas.job import JobSchema


class RecipeSchema(BaseSchemaOrm):
    id: int
    result_item_id: int
    result_item: ItemSchema
    # ingredients: list[IngredientSchema]
    job_id: int
    job: JobSchema

    receipe_pod_cost: int

    def __hash__(self) -> int:
        return self.id.__hash__()
