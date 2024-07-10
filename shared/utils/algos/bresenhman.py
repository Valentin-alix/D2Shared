from typing import Iterator


def bresenham_dofus(
    start_x: int, start_y: int, end_x: int, end_y: int, log: bool = False
) -> list[tuple[int, int]]:
    # taken from https://gist.github.com/SuperJudeFruit/ade08bda7c4ff31ee7298f4206cceeff#file-bresenham_dofus-py

    y_step = 0
    x_step = 0

    error = 0
    error_prev = 0

    y = start_y
    x = start_x
    ddy = 0
    ddx = 0
    dx = end_x - start_x
    dy = end_y - start_y

    result: list[tuple[int, int]] = []
    result.append((start_x, start_y))
    if dy < 0:
        y_step = -1
        dy = -dy
    else:
        y_step = 1
    if dx < 0:
        x_step = -1
        dx = -dx
    else:
        x_step = 1

    ddy = 2 * dy
    ddx = 2 * dx
    if ddx >= ddy:
        error_prev = error = dx
        for _ in range(dx):
            x += x_step
            error += ddy
            if error > ddx:
                y += y_step
                error -= ddx
                if error + error_prev < ddx:
                    result.append((x, y - y_step))
                elif error + error_prev > ddx:
                    result.append((x - x_step, y))
            result.append((x, y))
            error_prev = error
    else:
        error_prev = error = dy
        for _ in range(dy):
            y += y_step
            error += ddx
            if error > ddy:
                x += x_step
                error -= ddy
                if error + error_prev < ddy:
                    result.append((x - x_step, y))
                elif error + error_prev > ddy:
                    result.append((x, y - y_step))
            result.append((x, y))
            error_prev = error

    return result


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
