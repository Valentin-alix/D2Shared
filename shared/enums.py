from enum import Enum, IntEnum, StrEnum, auto

from EzreD2Shared.shared.consts.adaptative.positions import (
    ZAAPI_SALE_HOTEL_CATEGORY_POSITION,
    ZAAPI_VARIOUS_CATEGORY_POSITION,
    ZAAPI_WORKSHOP_CATEGORY_POSITION,
)


class ServerNameEnum(StrEnum):
    IMAGIRO = "Imagiro"


class AreaEnum(IntEnum):
    INCARNAM = 45
    ASTRUB = 18


class BreedEnum(IntEnum):
    ENI = 7
    ENU = 3


class CharacteristicEnum(IntEnum):
    PA = 1
    PM = 23
    PO = 19
    CHANCE = 13
    VITALITY = 11


class ElemEnum(IntEnum):
    ELEMENT_NEUTRAL = 0
    ELEMENT_EARTH = 1
    ELEMENT_FIRE = 2
    ELEMENT_WATER = 3
    ELEMENT_AIR = 4


class JobEnum(StrEnum):
    # harvest
    WOODCUTTER = "Bûcheron"
    ALCHIMIST = "Alchimiste"
    FISHERMAN = "Pêcheur"
    PEASANT = "Paysan"

    MINOR = "Minor"  # (not supported for harvest)
    # artisan
    SMITH = "Forgeron"
    SCULPTOR = "Sculpteur"
    SHOEMAKER = "Cordonnier"
    JEWELER = "Bijoutier"
    TAILOR = "Tailleur"
    HUNTER = "Chasseur"
    SHAPER = "Faconneur"
    TINKER = "Bricoleur"
    # mage
    SMITH_MAGE = "Forgemage"
    SCULPTOR_MAGE = "Sculptemage"
    SHOEMAKER_MAGE = "Cordomage"
    JEWELER_MAGE = "Joaillomage"
    TAILOR_MAGE = "Costumage"
    SHAPER_MAGE = "Façomage"


class ToDirection(int, Enum):
    TOP_LEFT = auto()
    TOP = auto()
    TOP_RIGHT = auto()
    BOT_LEFT = auto()
    BOT = auto()
    BOT_RIGHT = auto()
    RIGHT_TOP = auto()
    RIGHT = auto()
    RIGHT_BOT = auto()
    LEFT_TOP = auto()
    LEFT = auto()
    LEFT_BOT = auto()


class FromDirection(int, Enum):
    TOP_LEFT = auto()
    TOP = auto()
    TOP_RIGHT = auto()
    BOT_LEFT = auto()
    BOT = auto()
    BOT_RIGHT = auto()
    RIGHT_TOP = auto()
    RIGHT = auto()
    RIGHT_BOT = auto()
    LEFT_TOP = auto()
    LEFT = auto()
    LEFT_BOT = auto()
    WAYPOINT = auto()
    ZAAPI = auto()
    UNKNOWN = auto()


class DispellableEnum(IntEnum):
    IS_DISPELLABLE = 1
    IS_DISPELLABLE_ONLY_BY_DEATH = 2
    IS_NOT_DISPELLABLE = 3


class CategoryEnum(IntEnum):
    ALL = -1
    EQUIPMENT = 0
    CONSUMABLES = 1
    RESOURCES = 2
    QUEST = 3
    OTHER = 4
    COSMETICS = 5
    ECAFLIP_CARD = 238


class CategoryZaapiPosition(Enum):
    WORKSHOP = ZAAPI_WORKSHOP_CATEGORY_POSITION
    SALE_HOTEL = ZAAPI_SALE_HOTEL_CATEGORY_POSITION
    VARIOUS = ZAAPI_VARIOUS_CATEGORY_POSITION
