def read_input(file_name):
    with open(file_name, 'r') as f:
        return [line for line in f]


def solution_1(instructions) -> (int, bool):
    visited = set()
    instruction_pointer = 0
    acc = 0
    while True:
        current_line = instructions[instruction_pointer]
        print(f'executing {instruction_pointer}')
        if instruction_pointer in visited:
            return acc, False

        visited.add(instruction_pointer)
        op, val = current_line.strip().split(' ')
        if op == 'nop':
            instruction_pointer += 1
            print('nop')
        elif op == 'acc':
            instruction_pointer += 1
            acc += int(val)
        elif op == 'jmp':
            instruction_pointer += int(val)

        if instruction_pointer == len(instructions):
            return acc, True


def solution_2(instructions):
    for idx, line in enumerate(instructions):
        subbed = instructions[:]
        op, val = line.strip().split(' ')
        if op == 'nop':
            subbed[idx] = 'jmp ' + val
        elif op == 'jmp':
            subbed[idx] = 'nop ' + val

        if op == 'nop' or op == 'jmp':
            acc, ends = solution_1(subbed)
            if ends:
                return acc


def main():
    instructions = read_input('data/day8.txt')
    # print(solution_1(instructions))
    print(solution_2(instructions))


if __name__ == '__main__':
    main()
