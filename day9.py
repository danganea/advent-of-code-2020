def read_input(file_name):
    with open(file_name, 'r') as f:
        return [int(val) for val in f]


def solution_1(numbers, loopback):
    for curr_number, number in enumerate(numbers):
        if curr_number < loopback:
            continue

        start_loopback = curr_number - loopback - 1

        can_sum = False
        for i in range(start_loopback, curr_number):
            for j in range(i, curr_number):
                if numbers[i] + numbers[j] == number:
                    can_sum = True
        if can_sum == False:
            return curr_number, number


def solution_2(numbers, index):
    # Prefix sum would be better, but too lazy.
    goal = numbers[index]

    for i in range(index):
        for j in range(i + 1, index):
            if sum(numbers[i:j + 1]) == goal:
                return i, j


def main():
    numbers = read_input('data/day9.txt')
    # Solution 1
    index, number = solution_1(numbers, loopback=25)
    print(number)
    # Solution 2
    range = solution_2(numbers, index)
    low, high = range
    smallest = min(numbers[low:high + 1])
    highest = max(numbers[low:high + 1])
    print(smallest + highest)
    # 1006


if __name__ == '__main__':
    main()
