from collections import deque

from ...schemas.cell import CellSchema


def bfs(start: CellSchema, target: CellSchema) -> int:
    queue: deque[tuple[CellSchema, int]] = deque([(start, 0)])
    visited: set[CellSchema] = set()
    visited.add(start)

    while queue:
        (current_cell, distance) = queue.popleft()

        if current_cell == target:
            return distance

        for neighbor in current_cell.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    raise ValueError(f"Did not found dist for {start} to {target}")
