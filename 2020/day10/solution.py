# https://adventofcode.com/2020/day/10


def part_1(data: list[int]) -> int:
    """2400"""
    diffs = {}

    nums = sorted(data)
    nums.append(nums[-1]+3)
    prev = 0
    for num in nums:
        diff = num - prev
        diffs[diff] = diffs.setdefault(diff, 0) + 1
        prev = num

    return (diffs[1]*diffs[3])


def count_combos(connection_map, current, memo_map):
    if current in memo_map:
        return memo_map[current]

    if current not in connection_map:
        memo_map[current] = 0
        return 0

    options = connection_map.get(current, [])
    if not options:
        memo_map[current] = 1
        return 1

    total = 0
    for option in options:
        total += count_combos(connection_map, option, memo_map)

    memo_map[current] = total
    return total

def part_2(data: list[int]) -> int:
    """338510590509056"""
    can_connect = {
        0: [1,2,3]
    }

    for num in data:
        can_connect[num] = [
            n
            for n in data
            if n <= (num + 3) and n > num
        ]

    return count_combos(can_connect, 0, {})


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [
            int(line)
            for line in f.readlines()
        ]

    print(part_1(data))
    print(part_2(data))
