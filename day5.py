import math


def load_input(file_name):
    with open(file_name, 'r') as f:
        return [line.strip() for line in f]


def get_range(char, low, high):
    if char == 'F' or char == 'L':
        return low, int((low + high) / 2)
    else:
        return math.ceil((low + high) / 2), high


def solve_range(directions, low, high):
    for d in directions:
        low, high = get_range(d, low, high)

    assert low == high
    return low, high


def get_seat_id(row, column):
    return row * 8 + column


def boarding_pass_sol(boarding_pass):
    row, _ = solve_range(boarding_pass[:7], 0, 127)
    column, _ = solve_range(boarding_pass[7:], 0, 7)

    return get_seat_id(row, column)


def solution_1(all_passes):
    all_ids = [boarding_pass_sol(boarding_pass) for boarding_pass in all_passes]
    return all_ids


def solution_2(all_passes):
    all_ids = solution_1(all_passes)
    all_ids = sorted(all_ids)

    prev_id = all_ids[0]
    for id in all_ids[1:]:
        if id - prev_id > 1:
            return id - 1
        prev_id = id



if __name__ == '__main__':
    all_passes = load_input('data/day5.txt')
    print(max(solution_1(all_passes)))

    print(solution_2(all_passes))
