from D2Shared.shared.enums import SaleHotelQuantity
from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.type_item import TypeItemSchema


class ItemSchema(BaseSchemaOrm):
    id: int
    name: str
    type_item_id: int
    type_item: TypeItemSchema
    level: int
    weight: int
    icon_id: int | None = None
    is_saleable: bool

    def __hash__(self) -> int:
        return self.id.__hash__()

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.__str__()


class SellItemInfo(BaseSchemaOrm):
    item_id: int
    item: ItemSchema
    sale_hotel_quantities: list[SaleHotelQuantity]

    def __hash__(self) -> int:
        return self.item_id.__hash__()
