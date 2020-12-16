from collections import Counter
import copy


def read_grid(file_name):
    with open(file_name, 'r') as f:
        return [list(line.strip()) for line in f]


def count_neighbours(grid, index_r, index_c):
    counting = Counter()
    diffs = [x for x in range(-1, 2)]
    num_rows = len(grid)
    num_cols = len(grid[0])

    for row_diff in diffs:
        for col_diff in diffs:

            if 0 == row_diff == col_diff:  # Don't count current element
                continue

            r = index_r + row_diff
            c = index_c + col_diff

            if r < 0 or r >= num_rows or c < 0 or c >= num_cols:
                continue

            counting[grid[r][c]] += 1

    return counting


def solution_1(grid):
    changed = True

    while changed:
        changed = False

        new_grid = copy.deepcopy(grid)
        for r_idx, _ in enumerate(grid):
            for c_idx, _ in enumerate(grid[r_idx]):
                neighbours = count_neighbours(grid, r_idx, c_idx)

                current = grid[r_idx][c_idx]
                if current == 'L' and '#' not in neighbours:
                    new_grid[r_idx][c_idx] = '#'
                    changed = True
                elif current == '#' and (neighbours['#'] >= 4):
                    new_grid[r_idx][c_idx] = 'L'
                    changed = True
        grid = new_grid

    return sum([1 for row in grid for col in row if col == '#'])


def main():
    grid = read_grid('data/day11.txt')
    # print(grid)
    # print(count_neighbours(grid, 0, 0))
    print(solution_1(grid))


if __name__ == '__main__':
    main()
