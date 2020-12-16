from collections import Counter, defaultdict


def read_input(file_name):
    with open(file_name, 'r') as f:
        return [int(val) for val in f]


def solution_1(numbers):
    sorted_numbers = sorted(numbers)
    # Append device charger ( higher than max with 3)
    sorted_numbers = [0] + sorted_numbers + [max(sorted_numbers) + 3]
    prev = sorted_numbers[0]

    diffs = Counter()  # Overkill :)
    for number in sorted_numbers[1:]:
        print('diff {} number {} prev {}'.format(number - prev, number, prev))
        diffs[number - prev] += 1
        prev = number
    return diffs

def solution_2(numbers):
    sorted_numbers = sorted(numbers)
    # Append device charger ( higher than max with 3)
    sorted_numbers = [0] + sorted_numbers + [max(sorted_numbers) + 3]

    pd = [0] * len(sorted_numbers)
    pd[0] = 1

    # Amount of ways I can get to I is equal to sum of amount of ways I can get to all numbers within distance 3 of I
    # These can be at most three numbers, leaving the recurrence to be:
    # pd[i] = pd[i - 1] + pd[i - 2] + pd[i - 3]
    # Where pd[i] = 0 if i < 0 ; 0 if sorted_numbers[i] - prev_number > 3 and otherwise we calculate it
    for idx in range(1, len(sorted_numbers)) :

        for diff in range(1,4): # Check last three numbers
            new_idx = idx - diff #
            if new_idx < 0:
                continue
            if sorted_numbers[idx] - sorted_numbers[new_idx] > 3:
                continue
            pd[idx] += pd[new_idx]

    return pd[-1]





def main():
    numbers = read_input('data/day10.txt')
    diff_counter = solution_1(numbers)
    print(diff_counter[1] * diff_counter[3])
    arrangements = solution_2(numbers)
    print(arrangements)


if __name__ == '__main__':
    main()
