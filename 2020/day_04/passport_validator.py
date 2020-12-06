"""Passport validator."""

import os
import re


BATCH_TXT = 'batch.txt'
OPTIONAL = ['cid']
RANGES = {
    'byr': (1920, 2002),
    'iyr': (2010, 2020),
    'eyr': (2020, 2030),
    'cm': (150, 193),
    'in': (59, 76)
}
REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
YEAR_TYPES = ['byr', 'iyr', 'eyr']


def valid_passports():
    """Get list of valid passports."""
    raw_passports = _load_passports()
    parsed_passports = _parse_passports(raw_passports)
    complete_passports = _get_passports_with_required_fields(parsed_passports)
    return _valid_passports_filter(complete_passports)


def _get_passports_with_required_fields(passports: list):
    """Return list of passports that have the required fields."""
    valid_list = []
    for passport in passports:
        fields = set(passport.keys())
        if len(fields) == 8 and fields == set(REQUIRED_FIELDS + OPTIONAL):
            valid_list.append(passport)
        if len(fields) == 7 and fields == set(REQUIRED_FIELDS):
            valid_list.append(passport)
    return valid_list


def _load_passports():
    """Load passports from txt file."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), BATCH_TXT)
    f = open(filepath, 'r')
    raw_batch = f.read()
    f.close()
    return raw_batch


def _parse_passports(raw_batch: str):
    """Parse raw passports read from txt file. Returns dict."""
    passports = []
    batch_list = raw_batch.strip().split('\n\n')
    batch_matrix = [batch.replace('\n', ' ').split(' ') for batch in batch_list]

    for batch in batch_matrix:
        passport_dict = {}
        for field in batch:
            key_value = field.split(':')
            passport_dict.update({key_value[0]: key_value[1]})
        passports.append(passport_dict)

    return passports


def _validate_cid(val: str):
    """Validate credential_id."""
    return True


def _validate_eye(val: str):
    """Validate eye color."""
    return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def _validate_hair(val: str):
    """Validate hair color is a correctly formatted string."""
    return bool(re.match(r'#[0-9a-f]{6}\b', val))


def _validate_height(val: str):
    """Validate height is in inches or centimeters and is in a certain range."""
    height = None
    ht_range = None

    if 'cm' in val:
        ht_range = RANGES['cm']
        height = int(val[:3]) if val[:3].isnumeric() else None

    if 'in' in val:
        ht_range = RANGES['in']
        height = int(val[:2]) if val[:2].isnumeric() else None

    if height and ht_range:
        ht_min = ht_range[0]
        ht_max = ht_range[1]
        return ht_min <= height <= ht_max

    return False


def _validate_pid(val: str):
    """Validate passport id."""
    return len(val) == 9 and val.isnumeric()


def _validate_year(year: str, year_type: str):
    """Validate string year is a 4 digit number between a certain range."""
    if len(year) == 4 and year.isnumeric():
        year_ranges = RANGES[year_type]
        year_min = year_ranges[0]
        year_max = year_ranges[1]
        return year_min <= int(year) <= year_max

    return False


validators = {
    'byr': _validate_year,
    'iyr': _validate_year,
    'eyr': _validate_year,
    'hgt': _validate_height,
    'hcl': _validate_hair,
    'ecl': _validate_eye,
    'pid': _validate_pid,
    'cid': _validate_cid
}


def _valid_passports_filter(passports: list):
    """Validate values for passports that have all required fields."""
    valid = []

    for passport in passports:
        fields = list(passport.keys())
        is_valid = True

        for field in fields:
            validator = validators[field]
            params = {'val': passport[field]}

            if field in YEAR_TYPES:
                params = {'year': passport[field], 'year_type': field}

            if not validator(**params):
                is_valid = False
                break

        if is_valid:
            valid.append(passport)

    return valid


# print(valid_passports())
# print(len(valid_passports()))
