from D2Shared.shared.enums import Direction


def get_inverted_direction(direction: Direction) -> Direction:
    match direction:
        case Direction.LEFT:
            return Direction.RIGHT
        case Direction.RIGHT:
            return Direction.LEFT
        case Direction.TOP:
            return Direction.BOT
        case Direction.BOT:
            return Direction.TOP
