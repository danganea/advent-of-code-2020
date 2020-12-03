from collections import Counter


def test():
    lines = read_lines('data/day2_test.txt')
    assert (solution(lines, valid_1) == 2)
    assert(solution(lines, valid_2) == 1)


def valid_1(line):
    rule, name = line.split(':')
    interval, letter = rule.split(' ')
    low, high = interval.split('-')
    low, high = int(low), int(high)

    occurences = Counter(name)

    if low <= occurences[letter] <= high:
        return True

    return False


def valid_2(line):
    # Could reuse
    rule, name = line.split(':')
    name = name.strip()
    interval, letter = rule.split(' ')
    idx1, idx2 = interval.split('-')
    idx1, idx2 = int(idx1), int(idx2)

    return (name[idx1 - 1] == letter) != (name[idx2 - 1] == letter)


def solution(lines, valid_func):
    cnt = 0
    for line in lines:
        if valid_func(line):
            cnt += 1
            print(line)


    return cnt


def read_lines(file_name):
    with open(file_name, 'r') as f:
        return [line for line in f]


if __name__ == '__main__':
    test()
    lines = read_lines('data/day2.txt')
    print(f'Sol 1 {solution(lines, valid_1)}')
    print(f'Sol 2 {solution(lines, valid_2)}')
