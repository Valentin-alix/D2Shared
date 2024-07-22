from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.server import ServerSchema


class PriceSchema(BaseSchemaOrm):
    id: int
    item_id: int
    server_id: int
    average: float
    server: ServerSchema

    def __hash__(self) -> int:
        return self.id.__hash__()
