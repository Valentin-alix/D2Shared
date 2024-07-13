from __future__ import annotations

from D2Shared.shared.schemas.base import BaseSchemaOrm


class StatSchema(BaseSchemaOrm):
    id: int
    name: str
    weight: float
    runes: list[RuneSchema]

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.__str__()


class RuneSchema(BaseSchemaOrm):
    id: int
    name: str
    stat_id: int
    stat_quantity: int


class BaseLineSchema(BaseSchemaOrm):
    value: int
    stat_id: int
    stat: StatSchema


class LineSchema(BaseLineSchema):
    id: int
    spent_quantity: int
