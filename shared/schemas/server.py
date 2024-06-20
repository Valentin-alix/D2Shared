from shared.schemas.base import BaseSchemaOrm


class ServerSchema(BaseSchemaOrm):
    id: int
    name: str

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return self.id.__hash__()
