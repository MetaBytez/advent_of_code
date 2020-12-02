# https://adventofcode.com/2020/day/1
from utils.decorators import timed


@timed
def part_1() -> int:
    """633216"""
    with open('input.txt') as f:
        nums = {
            int(x)
            for x in f.readlines()
        }

    for num in nums:
        target = 2020 - num
        if target == num:
            continue

        if target in nums:
            return target*num


@timed
def part_1_old() -> int:
    """633216"""
    with open('input.txt') as f:
        nums = list(map(int, f.readlines()))

    for i, x in enumerate(nums):
        for j, y in enumerate(nums[i+1:]):
            if (x + y) == 2020:
                return x*y


@timed
def part_2() -> int:
    """68348924"""
    with open('input.txt') as f:
        nums = {
            int(x)
            for x in f.readlines()
        }

    for num_1 in nums:
        remainder = 2020 - num_1
        for num_2 in nums:
            if num_2 == num_1:
                continue
            num_3 = remainder - num_2
            if num_3 in nums and num_3 != num_1:
                return num_1*num_2*num_3


@timed
def part_2_old() -> int:
    """68348924"""
    with open('input.txt') as f:
        nums = list(map(int, f.readlines()))

    for i, x in enumerate(nums):
        for j, y in enumerate(nums[i+1:]):
            for k, z in enumerate(nums[j+1:]):
                if (x + y + z) == 2020:
                    return x*y*z


if __name__ == '__main__':
    print(part_1())
    print(part_2())
