"""Passport validator."""

import os


BATCH_TXT = 'batch.txt'
REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
OPTIONAL = ['cid']


def valid_passports():
    """Get list of valid passports."""
    raw_passports = _load_passports()
    parsed_passports = _parse_passports(raw_passports)
    return _filter_valid_passports(parsed_passports)


def _filter_valid_passports(passports: list):
    """Return list of valid passports from a list of passport dicts."""
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
