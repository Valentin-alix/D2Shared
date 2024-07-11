from collections import deque
from typing import Any

import numpy
from pydantic import BaseModel, ConfigDict, Field

from D2Shared.shared.consts.adaptative.consts import (
    GRID_CELL_HEIGHT,
    GRID_CELL_WIDTH,
)
from D2Shared.shared.entities.position import Position
from D2Shared.shared.enums import TypeCellEnum
from D2Shared.shared.schemas.region import RegionSchema


class CellSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    col: int = Field(frozen=True)
    row: int = Field(frozen=True)
    center_pos: Position = Field(frozen=True)
    type_cell: TypeCellEnum = TypeCellEnum.UNKNOWN

    _neighbors: list["CellSchema"] = []

    @property
    def neighbors(self) -> list["CellSchema"]:  # to avoid limit depth error
        return self._neighbors

    def get_region(
        self, offset: tuple[int, int, int, int] = (0, 0, 0, 0)
    ) -> RegionSchema:  # We use an area instead of a form for better performance when checking color of cell
        x_center, y_center = self.center_pos.to_xy()

        left_offset, right_offset, top_offset, bot_offset = offset
        area = RegionSchema(
            left=max(int(x_center - GRID_CELL_WIDTH // 4 - left_offset), 0),
            right=int(x_center + GRID_CELL_WIDTH // 4 + right_offset),
            top=max(int(y_center - GRID_CELL_HEIGHT // 4 - top_offset), 0),
            bot=int(y_center + GRID_CELL_HEIGHT // 4 + bot_offset),
        )
        return area

    @property
    def region_top(
        self,
    ) -> RegionSchema:
        """get region of top of cell

        Returns:
            RegionSchema: region of top of of cell
        """

        x_center, y_center = self.center_pos.to_xy()

        area = RegionSchema(
            left=int(x_center - GRID_CELL_WIDTH / 8) + 1,
            top=int(y_center - GRID_CELL_HEIGHT / 2 + GRID_CELL_HEIGHT / 8) + 1,
            right=int(x_center + GRID_CELL_WIDTH / 8) - 1,
            bot=int(y_center - GRID_CELL_HEIGHT / 8) - 1,
        )
        return area

    @property
    def points(self) -> numpy.ndarray:
        """numpy array of the cell

        Returns:
            numpy.ndarray
        """

        x_center, y_center = self.center_pos.to_xy()

        OFFSET = 5
        pts = numpy.array(
            [
                [x_center - GRID_CELL_WIDTH // 2 + OFFSET, y_center],
                [x_center, y_center - GRID_CELL_HEIGHT // 2 + OFFSET],
                [x_center + GRID_CELL_WIDTH // 2 - OFFSET, y_center],
                [x_center, y_center + GRID_CELL_HEIGHT // 2 - OFFSET],
            ],
            dtype=numpy.int32,
        )
        return pts

    def __hash__(self) -> int:
        return (self.row, self.col).__hash__()

    def __str__(self) -> str:
        return f"{self.col}:{self.row}"

    def __eq__(self, value: "Any") -> bool:
        return (
            isinstance(value, CellSchema)
            and self.col == value.col
            and self.row == value.row
        )

    def get_dist_cell(self, cell: "CellSchema") -> int:
        # using bfs algo https://en.wikipedia.org/wiki/Breadth-first_search
        queue: deque[tuple[CellSchema, int]] = deque([(self, 0)])
        visited: set[CellSchema] = set()
        visited.add(self)

        while queue:
            (current_cell, distance) = queue.popleft()

            if current_cell == cell:
                return distance

            for neighbor in current_cell.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        raise ValueError(f"Did not found dist for {self} to {cell}")

    def is_closer(self, cell: "CellSchema|None", target_cell: "CellSchema") -> bool:
        if cell is None:
            return True
        return self.get_dist_cell(target_cell) < cell.get_dist_cell(target_cell)
