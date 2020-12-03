"""Password validator."""

import os


PASSWORD_TXT = 'passwords.txt'


def valid_passwords():
    """Get list of valid passwords."""
    all_passwords = _load_passwords()
    valid_passwords = []

    for password in all_passwords:
        split_pw = password.split(': ')
        policy = _parse_policy(split_pw[0])
        pw = split_pw[1]
        if _is_valid(pw, policy):
            valid_passwords.append(password)

    return valid_passwords


def _is_valid(password: str, policy: dict):
    """Validation for solution 02: char must appear in only one of given positions."""
    char = policy.get('char')
    pos_1 = policy.get('pos_1')
    pos_2 = policy.get('pos_2')

    if password[pos_1] == char and password[pos_2] == char:
        return False

    return password[pos_1] == char or password[pos_2] == char


def _load_passwords():
    """Load passwords from txt file, return list."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), PASSWORD_TXT)
    f = open(filepath, 'r')
    passwords = f.read()
    f.close()
    return passwords.strip().split('\n')


def _parse_policy(policy: str):
    """Parse policy from string, return dict."""
    split_policy = policy.split(' ')
    required_char = split_policy[1]
    instances = split_policy[0].split('-')

    return {
        'char': required_char,
        'max': int(instances[1]),
        'min': int(instances[0]),
        'pos_1': int(instances[0]) - 1,
        'pos_2': int(instances[1]) - 1
    }


def _was_valid(password: str, policy: dict):
    """Validation for solution 01: char must appear in pw certain amount of times."""
    char_count = password.count(policy.get('char'))
    return policy.get('min') <= char_count <= policy.get('max')


# print(len(valid_passwords()))
