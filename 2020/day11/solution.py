# https://adventofcode.com/2020/day/


def count_neighbors_1(x, y, matrix, width, height):
    count = 0
    for s_x, s_y in [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (-1, 1),
        (1, -1),
        (-1, -1),
    ]:
        _x = x
        _y = y
        while True:
            _x += s_x
            _y += s_y

            if width - 1 < _x or _x < 0:
                break
            if height - 1 < _y or _y < 0:
                break
            if matrix[_y][_x] == '#':
                count += 1
                break
            if matrix[_y][_x] == 'L':
                break

    return count


def part_1(data: list[str]) -> int:
    """2243"""

    def count_neighbors(x, y, width, height, matrix):
        count = 0
        for _x, _y in [
            (x-1, y),
            (x+1, y),
            (x, y-1),
            (x, y+1),
            (x-1, y-1),
            (x-1, y+1),
            (x+1, y-1),
            (x+1, y+1),
        ]:
            if width <= _x or _x < 0:
                continue
            if height <= _y or _y < 0:
                continue

            if matrix[_y][_x] == '#':
                count += 1

        return count


    width = len(data[0])
    height = len(data)

    matrix = [
        list(row)
        for row in data
    ]
    changed = True
    while changed:
        changed = False
        new_matrix = []

        for y in range(height):
            row = []
            for x in range(width):
                if matrix[y][x] == '.':
                    row.append('.')
                    continue

                neighbors = count_neighbors(x, y, width, height, matrix)
                if matrix[y][x] == 'L' and neighbors == 0:
                    row.append('#')
                    changed = True

                elif matrix[y][x] == '#' and neighbors >= 4:
                    row.append('L')
                    changed = True

                else:
                    row.append(matrix[y][x])

            new_matrix.append(row)

        matrix = [
            list(row)
            for row in new_matrix
        ]

    total = 0
    for line in matrix:
        total += line.count('#')

    return total


def part_2(data: list[str]) -> int:
    """2027"""

    def count_neighbors(x, y, width, height, matrix):
        count = 0
        for d_x, d_y in [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
        ]:
            _x = x
            _y = y
            while True:
                _x += d_x
                _y += d_y

                if width <= _x or _x < 0:
                    break

                if height <= _y or _y < 0:
                    break

                if matrix[_y][_x] == '#':
                    count += 1
                    break

                if matrix[_y][_x] == 'L':
                    break

        return count


    width = len(data[0])
    height = len(data)

    matrix = [
        list(row)
        for row in data
    ]
    changed = True
    while changed:
        changed = False
        new_matrix = []

        for y in range(height):
            row = []
            for x in range(width):
                if matrix[y][x] == '.':
                    row.append('.')
                    continue

                neighbors = count_neighbors(x, y, width, height, matrix)
                if matrix[y][x] == 'L' and neighbors == 0:
                    row.append('#')
                    changed = True

                elif matrix[y][x] == '#' and neighbors >= 5:
                    row.append('L')
                    changed = True

                else:
                    row.append(matrix[y][x])

            new_matrix.append(row)

        matrix = [
            list(row)
            for row in new_matrix
        ]

    total = 0
    for line in matrix:
        total += line.count('#')

    return total


if __name__ == '__main__':
    with open('input.txt') as f:
        data = [
            line.strip()
            for line in f.readlines()
        ]

    print(part_1(data))
    print(part_2(data))
