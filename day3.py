def read_pattern(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f]


def solution(pattern, slope_right, slope_down):
    curr_r, curr_c = 0, 0
    trees = 0
    columns = len(pattern[0])
    while curr_r < len(pattern):
        is_tree = pattern[curr_r][curr_c] == '#'
        if is_tree:
            trees += 1
        curr_c = (curr_c + slope_right) % columns
        curr_r = curr_r + slope_down

    return trees


if __name__ == '__main__':
    pattern = read_pattern('data/day3.txt')

    # Part 1
    print(solution(pattern, 3, 1))

    # Part 2
    res = solution(pattern, 1, 1) * solution(pattern, 3, 1) * solution(pattern, 5, 1) * solution(pattern, 7,
                                                                                                               1, 2)
    print(res)
