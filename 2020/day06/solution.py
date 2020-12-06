# https://adventofcode.com/2020/day/6

from string import ascii_lowercase

def part_1() -> int:
    """6778"""
    ascii_set = set(ascii_lowercase)
    answers = set()
    total = 0
    with open('input.txt') as f:
        for group in f.read().split('\n\n'):
            answers = set(group.replace('\n', ''))
            total += len(ascii_set.intersection(answers))

    return total


def part_2() -> int:
    """3406"""
    answers = set(ascii_lowercase)
    total = 0
    with open('input.txt') as f:
        for group in f.read().split('\n\n'):
            for line_set in map(set, group.split('\n')):
                answers = answers.intersection(line_set)
            total += len(answers)
            answers = set(ascii_lowercase)

    return total


if __name__ == '__main__':
    print(part_1())
    print(part_2())
