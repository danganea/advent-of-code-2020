from typing import List

def get_numbers(file_name):
    with open(file_name, 'r') as f:
        return [int(line.strip()) for line in f]

def answer_2(numbers : List[int]) -> int:
    seen = set()
    NEEDED = 2020
    for number in numbers:
        seen.add(number)

    for number in numbers:
        if NEEDED - number in seen:
            return number * (NEEDED - number)

    return None


def answer_3(numbers) -> int:
    seen = set()
    NEEDED = 2020
    for number in numbers:
        seen.add(number)

    for idx_1 in range(len(numbers)):
        for idx_2 in range(idx_1 + 1,  len(numbers)):
            if NEEDED - numbers[idx_1] - numbers[idx_2] in seen:
                return numbers[idx_1] * numbers[idx_2] * (NEEDED - numbers[idx_1] - numbers[idx_2])


def test():
    TEST_INPUT = [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]

    EXPECTED_ANSWER_1 = 514579
    EXPECTED_ANSWER_2 = 241861950

    assert(answer_2(TEST_INPUT) == EXPECTED_ANSWER_1)

    assert(answer_3(TEST_INPUT) == EXPECTED_ANSWER_2)



if __name__ == '__main__':
    test()
    # Part 1
    numbers = get_numbers('data/day1.txt')
    print(answer_2(numbers))
    print(answer_3(numbers))

    # Part 2

