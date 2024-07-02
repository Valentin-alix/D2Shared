from D2Shared.shared.schemas.base import BaseSchemaOrm


class AreaSchema(BaseSchemaOrm):
    id: int
    name: str
    is_for_sub: bool

    def __hash__(self) -> int:
        return self.id.__hash__()
