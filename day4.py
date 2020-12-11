import re


def read_input(file_name):
    with open(file_name, 'r') as f:
        return [line for line in f]


NEEDED_KEYS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
ALL_KEYS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}


def test_validate_value():
    assert validate_value('byr', '2002')
    assert not validate_value('byr', '2003')

    assert validate_value('hgt', '60in')
    assert validate_value('hgt', '190cm')
    assert not validate_value('hgt', '190in')
    assert not validate_value('hgt', '190')

    assert validate_value('ecl', 'brn')
    assert not validate_value('ecl', 'wat')

    assert validate_value('pid', '000000001')
    assert not validate_value('pid', '0123456789')



def validate_value(key, value):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.

    height_regex_rule = r'^(\d*)(cm|in)'
    hcl_regex_rule = r'^#[a-z0-9]{6}'
    ecl_regex_rule = r'^(amb|blu|brn|gry|grn|hzl|oth)'
    pid_regex_rule = r'\d{9}$'

    if key == 'byr':
        return 1920 <= int(value) <= 2002
    elif key == 'iyr':
        return 2010 <= int(value) <= 2020
    elif key == 'eyr':
        return 2020 <= int(value) <= 2030
    elif key == 'hgt':
        match = re.match(height_regex_rule, value)

        if not match:
            return False

        if match.group(2) == 'in':
            return 59 <= int(match.group(1)) <= 76
        else:
            return 150 <= int(match.group(1)) <= 193

    elif key == 'hcl':
        return re.match(hcl_regex_rule, value)
    elif key == 'ecl':
        return re.match(ecl_regex_rule, value)
    elif key == 'pid':
        return re.match(pid_regex_rule, value)


def validate_passport(passport, should_validate):
    key_value_pairs = passport.split()

    items = dict()
    for kv in key_value_pairs:
        k, v = kv.split(':')
        if k in NEEDED_KEYS:
            items[k] = v

    found_keys = set(list(items.keys()))

    if found_keys == NEEDED_KEYS:
        if should_validate:
            return all([validate_value(k, v) for k, v in items.items()])
        else:
            return True
    return False


def solution(lines, validate_values=False):
    valid = 0
    passport_input = ''
    # Handle last item
    lines.append('\n')

    for line in lines:
        passport_input = passport_input + line
        if line == '\n':
            passport_input.replace('\n', ' ')
            valid = valid + validate_passport(passport_input, validate_values)
            passport_input = ''

    return valid


if __name__ == '__main__':
    test_validate_value()
    lines = read_input('data/day4.txt')
    print(solution(lines, validate_values=True))