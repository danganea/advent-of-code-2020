def read_input(file_name):
    with open(file_name, 'r') as f:
        return [line for line in f]


def count_any(inputs):
    assert inputs
    inputs = inputs.replace('\n', ' ')
    inputs = inputs.replace(' ', '')
    return len(set(inputs))


def count_all(inputs):
    assert inputs
    all_sets = inputs.split()
    result_set = set(all_sets[0])

    for s in all_sets:
        result_set = result_set.intersection(set(s))

    return len(result_set)


def solution(lines, everyone_answered=False):
    unique_count = 0
    temp_input = ''
    # Handle last item
    lines.append('\n')

    for line in lines:
        temp_input = temp_input + line
        if line == '\n' and temp_input.strip():
            if everyone_answered:
                unique_count += count_all(temp_input)
            else:
                unique_count += count_any(temp_input)

            temp_input = ''

    return unique_count


if __name__ == '__main__':
    lines = read_input('data/day6.txt')
    # lines = read_input('data/day6_test.txt')
    print(solution(lines, everyone_answered=False))
    print(solution(lines, everyone_answered=True))
