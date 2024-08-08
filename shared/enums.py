from enum import IntEnum, StrEnum, auto


class ServerNameEnum(StrEnum):
    IMAGIRO = "Imagiro"


class AreaEnum(StrEnum):
    INCARNAM = "Incarnam"
    ASTRUB = "Astrub"
    AMAKNA = "Amakna"
    BONTA = "Bonta"
    CANIA_PLAIN = "Plaines de Cania"
    BRAKMAR = "Brâkmar"
    SIDIMOTE_LAND = "Landes de Sidimote"
    OTOMAI_ISLAND = "Île d'Otomaï"
    FRIGOST_ISLAND = "Île de Frigost"
    KOALAK_MONTAIN = "Montagne des Koalaks"


class CharacteristicEnum(StrEnum):
    PA = "Pa"
    PM = "Pm"
    PO = "Po"
    CHANCE = "Chance"
    VITALITY = "Vitalité"


class ElemEnum(StrEnum):
    ELEMENT_NEUTRAL = "Neutre"
    ELEMENT_EARTH = "Terre"
    ELEMENT_FIRE = "Feu"
    ELEMENT_WATER = "Eau"
    ELEMENT_AIR = "Air"


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


class ToDirection(IntEnum):
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


class FromDirection(IntEnum):
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


class CategoryEnum(IntEnum):
    ALL = -1
    EQUIPMENT = 0
    CONSUMABLES = 1
    RESOURCES = 2
    QUEST = 3
    OTHER = 4
    COSMETICS = 5
    ECAFLIP_CARD = 238


class CategoryZaapiEnum(IntEnum):
    WORKSHOP = auto()
    SALE_HOTEL = auto()
    VARIOUS = auto()


class TypeCellEnum(IntEnum):
    UNKNOWN = auto()
    NORMAL = auto()
    VOID = auto()
    OPAQUE = auto()
    OCCUPED = auto()


class SaleHotelQuantity(IntEnum):
    ONE = 1
    TEN = 10
    HUNDRED = 100
