from D2Shared.shared.enums import CategoryEnum
from D2Shared.shared.schemas.base import BaseSchemaOrm


class TypeItemSchema(BaseSchemaOrm):
    id: int
    name: str
    category: CategoryEnum

    def __hash__(self) -> int:
        return self.id.__hash__()
