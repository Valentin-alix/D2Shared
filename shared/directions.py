from EzreD2Shared.shared.enums import FromDirection, ToDirection


def get_inverted_direction(direction: ToDirection) -> FromDirection:
    match direction:
        case ToDirection.LEFT_TOP:
            return FromDirection.RIGHT_TOP
        case ToDirection.LEFT:
            return FromDirection.RIGHT
        case ToDirection.LEFT_BOT:
            return FromDirection.RIGHT_BOT

        case ToDirection.RIGHT_TOP:
            return FromDirection.LEFT_TOP
        case ToDirection.RIGHT:
            return FromDirection.LEFT
        case ToDirection.RIGHT_BOT:
            return FromDirection.LEFT_BOT

        case ToDirection.TOP_LEFT:
            return FromDirection.BOT_LEFT
        case ToDirection.TOP:
            return FromDirection.BOT
        case ToDirection.TOP_RIGHT:
            return FromDirection.BOT_RIGHT

        case ToDirection.BOT_LEFT:
            return FromDirection.TOP_LEFT
        case ToDirection.BOT:
            return FromDirection.TOP
        case ToDirection.BOT_RIGHT:
            return FromDirection.TOP_RIGHT
