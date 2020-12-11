"""Jolt module."""

import json
import os


ADAPTOR_JSON = 'adaptors.json'


def jolt_diffs():
    """Get jolt diffs."""
    adaptors = _load_adaptors()
    jolt_map = {3: 1}
    prev_adaptor = 0

    for adaptor in adaptors:
        diff = adaptor - prev_adaptor

        if jolt_map.get(diff):
            jolt_map[diff] += 1
        else:
            jolt_map[diff] = 1

        prev_adaptor = adaptor

    return jolt_map


def _load_adaptors():
    """Load adaptors from json file. Return sorted list."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), ADAPTOR_JSON)
    f = open(filepath, 'r')
    adaptors = json.load(f)
    f.close()
    return sorted(adaptors)


# SOLUTION 1 | 29 * 71 = 2059
# jolts = jolt_diffs()
# print(jolts)
# print(jolts.get(1) * jolts.get(3))
