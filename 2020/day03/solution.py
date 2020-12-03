# https://adventofcode.com/2020/day/3

from functools import reduce
from typing import List, Tuple


def count_trees(slope: Tuple[int, int], tree_map: List[str]) -> int:
    x_slope, y_slope = slope
    num_rows = len(tree_map)
    row_len = len(tree_map[0])
    tree_count = 0

    for stops in range(1, (num_rows//y_slope)):
        x, y = x_slope*stops, y_slope*stops
        x = x % row_len
        if tree_map[y][x] == '#':
            tree_count += 1
    return tree_count


def part_1():
    """250"""
    with open('input.txt') as f:
        return count_trees(
            (3,1),
            [
                line.strip()
                for line in f.readlines()
            ]
        )


def part_2():
    """1592662500"""
    slopes = [
        (1,1),
        (3,1),
        (5,1),
        (7,1),
        (1,2),
    ]

    with open('input.txt') as f:
        tree_map = [
            line.strip()
            for line in f.readlines()
        ]

    return reduce(
        lambda x, y: x*y,
        [
            count_trees(slope, tree_map)
            for slope in slopes
        ]
    )


if __name__ == '__main__':
    print(part_1())
    print(part_2())
