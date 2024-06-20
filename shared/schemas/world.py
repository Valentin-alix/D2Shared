from shared.schemas.base import BaseSchemaOrm


class WorldSchema(BaseSchemaOrm):
    id: int
    name: str

    def __hash__(self) -> int:
        return self.id.__hash__()
