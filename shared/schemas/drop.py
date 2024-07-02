from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.item import ItemSchema


class DropSchema(BaseSchemaOrm):
    id: int
    monster_id: int
    # monster: "MonsterSchema"
    item_id: int
    item: ItemSchema
    percentage: float

    def __hash__(self) -> int:
        return self.id.__hash__()
