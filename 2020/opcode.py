class BootLoop(Exception):
    pass


class OpCodeMachine:

    def __init__(self):
        self.accumulator = 0
        self.instruction_index = 0
        self.code_length = 0
        self.stack_trace: list[int] = []
        self._executed: set[int] = set()

    def run(self, code: list[str], debug: bool = False) -> int:
        self.__init__()
        self.code_length = len(code)

        while self.instruction_index < self.code_length:
            self.stack_trace.append(self.instruction_index)

            if self.instruction_index in self._executed:
                raise BootLoop('Infinite loop found!')

            if debug:
                print(f'Running: {code[self.instruction_index]} - ', end='')

            idx = self.instruction_index
            self._execute(code[self.instruction_index])
            self._executed.add(idx)

            if debug:
                print(self.accumulator)


        return self.accumulator

    def _execute(self, instruction: str) -> None:
        opcode, val = instruction.split()

        if opcode == 'nop':
            pass
        elif opcode == 'acc':
            self.accumulator += int(val)
        elif opcode == 'jmp':
            self.instruction_index += int(val)
            return
        self.instruction_index += 1
