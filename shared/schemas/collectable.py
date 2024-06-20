from EzreD2Shared.shared.schemas.base import BaseSchemaOrm
from EzreD2Shared.shared.schemas.item import ItemSchema
from EzreD2Shared.shared.schemas.job import JobSchema


class CollectableSchema(BaseSchemaOrm):
    id: int

    item_id: int
    item: ItemSchema

    job_id: int
    job: JobSchema


class CollectableMapInfoSchema(BaseSchemaOrm):
    collectable_id: int
    map_id: int
    collectable: CollectableSchema
    # map: "MapSchema"
    count: int
