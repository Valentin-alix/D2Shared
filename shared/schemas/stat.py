from __future__ import annotations


from D2Shared.shared.schemas.base import BaseSchemaOrm


class StatSchema(BaseSchemaOrm):
    id: int
    name: str
    weight: float


class RuneSchema(BaseSchemaOrm):
    id: int
    name: str
    stat_id: int
    stat: StatSchema
    stat_quantity: int


class LineSchema(BaseSchemaOrm):
    value: int
    stat_id: int
    stat: StatSchema
