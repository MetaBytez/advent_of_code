# https://adventofcode.com/2020/day/8

from opcode import BootLoop, OpCodeMachine        

def part_1() -> int:
    """1766"""
    op_machine = OpCodeMachine()
    with open('input.txt') as f:
        lines = [
            line.strip()
            for line in f.readlines()
        ]
    try:
        op_machine.run(lines)
    except BootLoop:
        return op_machine.accumulator

def part_2() -> int:
    """1639"""
    op_machine = OpCodeMachine()
    with open('input.txt') as f:
        lines = [
            line.strip()
            for line in f.readlines()
        ]

    code = list(lines)
    for i in range(len(lines)):
        opcode, val = code[i].split()
        if opcode == 'nop':
            code[i] = 'jmp ' + val
        elif opcode == 'jmp':
            code[i] = 'nop ' + val
        else:
            continue

        try:
            op_machine.run(code)
            return op_machine.accumulator
        except BootLoop:
            code = list(lines)

if __name__ == '__main__':
    print(part_1())
    print(part_2())