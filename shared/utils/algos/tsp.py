import itertools
from typing import Callable, TypeVar


def solve_tsp_dynamic(
    distance_matrix: list[list], from_first=False, to_last=False
) -> tuple[float, list[int]]:
    memo = {
        (frozenset([0, index + 1, len(distance_matrix) - 1]), index + 1): (
            dist,
            [0, index + 1, len(distance_matrix) - 1],
        )
        for index, dist in enumerate(distance_matrix[0][1:-1])
    }  # Memoize the distance from start pos to all other pos

    for group_count in range(2, len(distance_matrix) - 1):
        memo_curr = {}
        for subset in [
            frozenset(combination) | {0} | {len(distance_matrix) - 1}
            for combination in itertools.combinations(
                range(1, len(distance_matrix) - 1), group_count
            )  # Get all combinations of group count
        ]:
            for pos_index in subset - {0} - {len(distance_matrix) - 1}:
                memo_curr[(subset, pos_index)] = min(
                    [
                        (
                            memo[(subset - {pos_index}, pos_index_subset_bis)][0]
                            + distance_matrix[pos_index_subset_bis][pos_index],
                            memo[(subset - {pos_index}, pos_index_subset_bis)][1][:-1]
                            + [pos_index]
                            + [len(distance_matrix) - 1],
                        )
                        for pos_index_subset_bis in subset
                        if pos_index_subset_bis != 0
                        and pos_index_subset_bis != pos_index
                        and pos_index_subset_bis != len(distance_matrix) - 1
                    ]
                )
        memo = memo_curr

    res = min(
        [
            (
                memo[position][0]
                + (distance_matrix[0][position[1]] if from_first else 0)
                + (distance_matrix[-1][position[1]] if to_last else 0),
                memo[position][1],
            )
            for position in iter(memo)
        ]
    )
    return res


T = TypeVar("T")


def greedy_algorithm(vertexs: list[T], dist_func: Callable[[T, T], float]) -> list[T]:
    if len(vertexs) == 0:
        return vertexs

    optimal_path = [vertexs.pop(0)]

    while len(vertexs) > 0:
        near_vertex = sorted(
            vertexs, key=lambda elem: dist_func(elem, optimal_path[-1])
        )[0]
        optimal_path.append(near_vertex)
        vertexs = [elem for elem in vertexs if elem != near_vertex]

    return optimal_path
