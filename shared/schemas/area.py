from D2Shared.shared.schemas.base import BaseSchemaOrm


class AreaSchema(BaseSchemaOrm):
    id: int
    name: str
    is_for_sub: bool

    def __hash__(self) -> int:
        return self.id.__hash__()

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.__str__()
