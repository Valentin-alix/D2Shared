from D2Shared.shared.schemas.base import BaseSchemaOrm


class JobSchema(BaseSchemaOrm):
    id: int
    name: str

    def __hash__(self) -> int:
        return self.id.__hash__()

    def __str__(self) -> str:
        return self.name
