# general
from ...consts.adaptative.consts import (
    LINE_COUNT,
    LINE_END_X,
    LINE_HEIGHT,
    LINE_START_X,
    LINES_START_Y,
)
from ...schemas.region import RegionSchema

INVENTORY_RIGHT_CROSS_REGION = RegionSchema(left=1530, top=25, right=1588, bot=112)
ICON_CHARACTERISTIC_REGION = RegionSchema(left=1315, top=880, right=1600, bot=940)
EMPTY_REGION = RegionSchema(left=1, top=1, right=295, bot=1000)
CONTENT_REGION = RegionSchema(left=328, top=0, right=1591, bot=892)
CENTER_LARGE_V_REGION = RegionSchema(left=700, top=250, right=1275, bot=890)
CROSS_MAP = RegionSchema(left=1845, right=1919, top=0, bot=40)
INFO_MODAL_REGION = RegionSchema(left=0, top=525, right=400, bot=800)
AREA_BARS_RIGHT_SIDE = RegionSchema(left=1730, top=105, right=1915, bot=985)
CHAT_REGION = RegionSchema(left=0, top=600, right=750, bot=990)

CROSS_CONNECTIO_WARNING = RegionSchema(left=1231, top=160, right=1273, bot=200)
CROSS_POPUP_INFO = RegionSchema(left=1100, top=350, right=1300, bot=500)
CROSS_INFO_WIN_FIGHT = RegionSchema(left=1225, right=1300, bot=730, top=690)
CROSS_INFO_LOSE_FIGHT = RegionSchema(left=1103, top=695, right=1180, bot=724)

# INVENTORY
INVENTORY_FIRST_SLOT_REGION = RegionSchema(left=1259, top=157, right=1311, bot=209)
LEFT_INVENTORY_REGION = RegionSchema(left=374, top=178, bot=772, right=673)
RIGHT_INVENTORY_SALE_HOTEL = RegionSchema(left=1255, top=153, right=1552, bot=744)

INVENTORY_BAR = RegionSchema(left=1282, top=824, right=1398, bot=828)

INFO_BAR_REGION = RegionSchema(top=998, bot=1004, left=834, right=1302)
INFO_BAR_FIGHT_REGION = RegionSchema(top=991, bot=997, left=841, right=1303)

# harvest
CONTENT_REGION_COLLECTABLE = RegionSchema(left=360, top=25, right=1561, bot=874)

# movements
INFO_MAP_REGION = RegionSchema(left=10, top=10, right=300, bot=75)
ZONE_TEXT_REGION = RegionSchema(left=10, top=10, right=300, bot=43)
MAP_POSITION_REGION = RegionSchema(left=14, top=47, right=100, bot=75)

# sale hotel
SALE_HOTEL_FILTER_CHECK_REGION = RegionSchema(left=1250, top=822, right=1283, bot=850)
SALE_HOTEL_QUANTITY_REGION = RegionSchema(left=475, top=287, right=511, bot=305)

SALE_HOTEL_FIRST_PRICE_REGION = RegionSchema(left=515, top=525, right=580, bot=550)
SALE_HOTEL_FIRST_QUANTITY_REGION = RegionSchema(left=450, top=522, right=485, bot=545)

SALE_HOTEL_SECOND_PRICE_REGION = RegionSchema(left=515, top=565, right=580, bot=590)
SALE_HOTEL_SECOND_QUANTITY_REGION = RegionSchema(left=450, top=565, right=485, bot=590)

SALE_HOTEL_THIRD_PRICE_REGION = RegionSchema(left=515, top=605, right=580, bot=630)
SALE_HOTEL_THIRD_QUANTITY_REGION = RegionSchema(left=450, top=610, right=485, bot=635)

SALE_HOTEL_PLACE_SELL_REGION = RegionSchema(left=380, top=390, right=590, bot=440)
SALE_HOTEL_ONE_QUANTITY_REGION = RegionSchema(left=485, top=307, right=506, bot=335)
SALE_HOTEL_TEN_QUANTITY_REGION = RegionSchema(left=485, top=340, right=506, bot=356)
SALE_HOTEL_HUNDRED_QUANTITY_REGION = RegionSchema(left=485, top=365, right=515, bot=383)

SALE_HOTEL_AVAILABLE_SLOT_REGION = RegionSchema(left=627, top=821, right=729, bot=843)

CROSS_SALE_HOTEL_INVENTORY_RIGHT = RegionSchema(left=1540, top=40, right=1580, bot=80)

# fight
IN_FIGHT_REGION = RegionSchema(left=1430, top=970, right=1470, bot=1005)
END_FIGHT_MODAL_REGION = RegionSchema(left=870, top=650, right=1150, bot=750)
END_TURN_REGION = RegionSchema(left=1315, top=907, right=1465, bot=970)
CREATURE_MODE_REGION = RegionSchema(left=1300, top=970, right=1450, bot=1020)
HELP_LOCK_FIGHT_PREP_REGION = RegionSchema(left=1330, top=860, right=1420, bot=910)
PA_REGION = RegionSchema(left=742, top=977, right=767, bot=999)
RIP_REGION = RegionSchema(left=735, top=450, right=865, bot=595)


MERGE_AREA = RegionSchema(left=961, top=212, right=1142, bot=232)
HISTORY_AREA = RegionSchema(left=315, top=126, right=641, bot=835)
LINE_AREAS = [
    RegionSchema(
        left=LINE_START_X,
        top=int((LINE_HEIGHT * line) + LINES_START_Y),
        right=LINE_END_X,
        bot=int((LINE_HEIGHT * (line + 1)) + LINES_START_Y),
    )
    for line in range(LINE_COUNT)
]
