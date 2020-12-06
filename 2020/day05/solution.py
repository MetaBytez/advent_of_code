# https://adventofcode.com/2020/day/5


def get_seat_id(boarding_pass: str) -> int:
    bin_string = ''
    for c in boarding_pass:
        if c in ['B', 'R']:
            bin_string += '1'
        else:
            bin_string += '0'

    row = int(bin_string[:7], base=2)
    col = int(bin_string[7:], base=2)

    return row*8 + col

def part_1() -> int:
    """894"""
    with open('input.txt') as f:
        return max([
            get_seat_id(line.strip())
            for line in f.readlines()
        ])


def part_2() -> int:
    """579"""
    with open('input.txt') as f:
        pass_ids = sorted([
            get_seat_id(line.strip())
            for line in f.readlines()
        ])
    valid_seats = set(range(pass_ids[0], pass_ids[-1]))
    return valid_seats.difference(set(pass_ids)).pop()


if __name__ == '__main__':
    print(part_1())
    print(part_2())
