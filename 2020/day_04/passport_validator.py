"""Passport validator."""

import os
import re

from utils.enum import enum


BATCH_TXT = 'batch.txt'
OPTIONAL = ['cid']
REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
RANGES = {
    'byr': (1920, 2002),
    'iyr': (2010, 2020),
    'eyr': (2020, 2030),
    'cm': (150, 193),
    'in': (59, 76)
}
YEAR_TYPES = enum(
    'year_types',
    BYR='byr',
    IYR='iyr',
    EYR='eyr'
)


def valid_passports():
    """Get list of valid passports."""
    raw_passports = _load_passports()
    parsed_passports = _parse_passports(raw_passports)
    return _filter_passports_with_required_fields(parsed_passports)


def _filter_passports_with_required_fields(passports: list):
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


def _validate_cid(credential_id: str):
    """Validate credential_id."""
    pass


def _validate_eye(eye_color: str):
    """Validate eye color."""
    return eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_hair(hair_color: str):
    """Validate hair color is a correctly formatted string."""
    return bool(re.match(r'#[0-9a-f]{6}\b'))


def _validate_height(height_value: str):
    """Validate height is in inches or centimeters and is in a certain range."""
    height = None
    ht_range = None

    if 'cm' in height_value:
        ht_range = RANGES['cm']
        height = len(height_value[:3])

    if 'in' in height_value:
        ht_range = RANGES['in']
        height = len(height_value[:2])

    if height and ht_range:
        ht_min = ht_range[0]
        ht_max = ht_range[1]
        return ht_min <= height <= ht_max

    return False


def _validate_pid(passport_id: str):
    """Validate passport id."""
    pass

def _validate_year(year: str, year_type: str):
    """Validate string year is a 4 digit number between a certain range."""
    if len(year) == 4 and year.isnumeric():
        year_ranges = RANGES[year_type]
        year_min = year_ranges[0]
        year_max = year_ranges[1]
        return year_min <= int(year) <= year_max

    return False
