import math
from typing import Any

from pydantic import BaseModel, ConfigDict

from ..schemas.region import RegionSchema


class Position(BaseModel):
    model_config = ConfigDict(frozen=True)

    x_pos: int
    y_pos: int

    def __repr__(self) -> str:
        return str((self.x_pos, self.y_pos))

    def __hash__(self) -> int:
        return (self.x_pos, self.y_pos).__hash__()

    def __eq__(self, value: "Any") -> bool:
        return (
            isinstance(value, Position)
            and self.x_pos == value.x_pos
            and self.y_pos == value.y_pos
        )

    def to_xy(self) -> tuple[int, int]:
        return self.x_pos, self.y_pos

    def get_distance(self, other: "Position") -> float:
        return math.dist([self.x_pos, self.y_pos], [other.x_pos, other.y_pos])

    def is_in_region(self, area: RegionSchema) -> bool:
        return (
            self.x_pos > area.left
            and self.x_pos < area.right
            and self.y_pos > area.top
            and self.y_pos < area.bot
        )
