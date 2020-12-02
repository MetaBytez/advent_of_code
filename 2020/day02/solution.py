# https://adventofcode.com/2020/day/2
import re

PARSER = re.compile(r'(\d+)-(\d+) (\w): (\w+)')


def part_1():
    """572"""
    valid_count = 0
    with open('input.txt') as f:
        for line in f.readlines():
            lower, upper, letter,  password = PARSER.match(line).groups()
            occurences = password.count(letter)
            if int(lower) <= occurences and occurences <= int(upper):
                valid_count += 1

        return valid_count


def part_2():
    """306"""
    valid_count = 0
    with open('input.txt') as f:
        for line in f.readlines():
            position_1, position_2, letter,  password = PARSER.match(line).groups()
            position_1 = int(position_1) - 1
            position_2 = int(position_2) - 1

            if (
                (password[position_1] == letter and password[position_2] != letter)
                or
                (password[position_1] != letter and password[position_2] == letter)
            ):
                valid_count += 1

        return valid_count


if __name__ == '__main__':
    print(part_1())
    print(part_2())
