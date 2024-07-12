from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.item import ItemSchema
from D2Shared.shared.schemas.job import JobSchema


class CollectableSchema(BaseSchemaOrm):
    id: int

    item_id: int
    item: ItemSchema

    job_id: int
    job: JobSchema

    def __str__(self) -> str:
        return self.item.name

    def __repr__(self) -> str:
        return self.__str__()


class CollectableMapInfoSchema(BaseSchemaOrm):
    collectable_id: int
    map_id: int
    collectable: CollectableSchema
    count: int

    def __str__(self) -> str:
        return f"{self.count} {str(self.collectable)}"

    def __repr__(self) -> str:
        return self.__str__()
