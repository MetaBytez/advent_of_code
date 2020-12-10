# https://adventofcode.com/2020/day/9

from itertools import combinations


def find_invalid(nums: list[int], preamble: int) -> tuple[int, int]:
    valid_nums = {}

    for i in range(preamble):
        for j in range(i):
            valid_nums[j].add(nums[j]+nums[i])
        valid_nums[i] = set()

    for offset, num in enumerate(nums[preamble:]):
        found = False
        for sums in valid_nums.values():
            if num in sums:
                found = True
            sum_num = nums[(preamble + offset) - len(sums) -1]
            sums.add(sum_num+num)

        if not found:
            return num

        valid_nums[offset % preamble] = set()

def part_1() -> int:
    """27911108"""
    with open('input.txt') as f:
        nums = list(map(int, f.readlines()))

    return find_invalid(nums, 25)


def part_2() -> int:
    with open('input.txt') as f:
        nums = list(map(int, f.readlines()))

    target = find_invalid(nums, 25)
    head, tail = 0, 0
    summed = nums[0]

    while summed != target:
        if summed < target:
            tail += 1
            summed += nums[tail]
        elif summed > target:
            summed -= nums[head]
            head += 1

    return min(nums[head:tail+1]) + max(nums[head:tail+1])


def part_1_old() -> int:
    """27911108"""
    with open('input.txt') as f:
        nums = list(map(int, f.readlines()))

    preamble = 25
    valid_nums = list(nums[:25])
    idx = 0

    for num in nums[25:]:
        if not any([
            x+y == num
            for x,y in combinations(valid_nums, 2)
        ]):
            return num
        else:
            valid_nums[idx] = num
            idx = (idx + 1) % preamble


def part_2_old() -> int:
    """4023754"""
    with open('input.txt') as f:
        nums = list(map(int, f.readlines()))

    preamble = 25
    init = preamble
    valid_nums = [0 for i in range(preamble)]
    idx = 0
    target = 0
    for num in nums:
        if init:
            valid_nums[idx] = num
            idx = (idx+1)%preamble
            init -= 1
        elif not any([
                x+y == num
                for x,y in combinations(valid_nums, 2)
            ]):
                target = num
                break
        else:
            valid_nums[idx] = num
            idx = (idx+1)%preamble

    for i in range(nums.index(target) -1 , -1, -1):
        for j in range(i-1, -1, -1):
            if sum(nums[j:i]) == target:
                a = sorted(nums[j:i])
                return a[0] + a[-1]


if __name__ == '__main__':
    print(part_1())
    print(part_2())