# https://adventofcode.com/2020/day/


def part_1(data: list[str]) -> int:
    """1221"""
    DIRECTIONS = {
        0: (1, 0),
        90: (0, -1),
        180: (-1, 0),
        270: (0, 1)
    }
    INSTRUCTIONS = {
        'N': lambda x, y, rot, val: (x, y+val, rot),
        'E': lambda x, y, rot, val: (x+val, y, rot),
        'S': lambda x, y, rot, val: (x, y-val, rot),
        'W': lambda x, y, rot, val: (x-val, y, rot),
        'L': lambda x, y, rot, val: (x, y, (rot - val) % 360),
        'R': lambda x, y, rot, val: (x, y, (rot + val) % 360),
        'F': lambda x, y, rot, val: (x+(DIRECTIONS[rot][0]*val), y+(DIRECTIONS[rot][1]*val), rot)
    }
    
    ship_x, ship_y = 0, 0
    rotation = 0
    for line in data:
        cmd = line[0]
        val = int(line[1:])
        ship_x, ship_y, rotation = INSTRUCTIONS[cmd](ship_x, ship_y, rotation, val)
    
    return abs(ship_x) + abs(ship_y)

def part_2(data: list[str]) -> int:
    """59435"""
    INSTRUCTIONS = {
        'N': lambda x, y, val: (x, y+val),
        'E': lambda x, y, val: (x+val, y),
        'S': lambda x, y, val: (x, y-val),
        'W': lambda x, y, val: (x-val, y),
    }

    ship_x, ship_y = 0, 0
    waypoint_x, waypoint_y = 10, 1
    rotation = 0

    for line in data:
        cmd = line[0]
        val = int(line[1:])
        if cmd in INSTRUCTIONS:
            waypoint_x, waypoint_y = INSTRUCTIONS[cmd](waypoint_x, waypoint_y, val)
        elif cmd == 'L':
            for __ in range(val//90):
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
        elif cmd == 'R':
            for __ in range(val//90):
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
        else:
            ship_x, ship_y = ship_x + (waypoint_x*val), ship_y + (waypoint_y*val)

    return abs(ship_x) + abs(ship_y)    

if __name__ == '__main__':
    with open('input.txt') as f:
        data = [
            line.strip()
            for line in f.readlines()
        ]

    print(part_1(data))
    print(part_2(data))
