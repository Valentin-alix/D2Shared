from typing import Iterator


def bresenham(
    start_x: int, start_y: int, end_x: int, end_y: int
) -> Iterator[tuple[int, int]]:
    """Yield integer coordinates on the line from (x0, y0) to (x1, y1).

    Input coordinates should be integers.

    The result will contain both the start and the end point.
    """

    dist_x = end_x - start_x
    dist_y = end_y - start_y

    x_sign = 1 if dist_x > 0 else -1
    y_sign = 1 if dist_y > 0 else -1

    dist_x = abs(dist_x)
    dist_y = abs(dist_y)

    # vérifier dans quel sens la pente est le plus incliné
    if dist_x > dist_y:
        xx, xy, yx, yy = x_sign, 0, 0, y_sign
    else:
        dist_x, dist_y = dist_y, dist_x
        xx, xy, yx, yy = 0, y_sign, x_sign, 0

    decision_error = 2 * dist_y - dist_x
    y = 0

    for x in range(dist_x + 1):
        yield start_x + x * xx + y * yx, start_y + x * xy + y * yy
        if decision_error >= 0:
            y += 1
            decision_error -= 2 * dist_x
        decision_error += 2 * dist_y
