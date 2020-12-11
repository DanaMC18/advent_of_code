"""Jolt module."""

import json
import os


adapter_JSON = 'adapters.json'


def _load_adapters():
    """Load adapters from json file. Return sorted list."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), adapter_JSON)
    f = open(filepath, 'r')
    adapters = json.load(f)
    f.close()
    return sorted(adapters)


# SOLUTION 1 | 29 * 71 = 2059
def jolt_diffs(adapters: list):
    """Get jolt differences."""
    adapters = _load_adapters()
    jolt_map = {3: 1}
    prev_adapter = 0

    for adapter in adapters:
        diff = adapter - prev_adapter

        if jolt_map.get(diff):
            jolt_map[diff] += 1
        else:
            jolt_map[diff] = 1

        prev_adapter = adapter

    return jolt_map
# jolts = jolt_diffs()
# print(jolts)
# print(jolts.get(1) * jolts.get(3))


# SOLUTION 2 | 86812553324672
def _get_arrangement_counts(neighbors_map: dict):
    """Get number of arrangments per adapter."""
    arrangements = {0: 1}
    for adapter, neighbors in neighbors_map.items():
        for neighbor in neighbors:
            if neighbor in arrangements:
                arrangements[neighbor] += arrangements[adapter]
            else:
                arrangements[neighbor] = arrangements[adapter]
    return arrangements


def _get_neighbors(adapters: list):
    """Get possible next adapters ("neighbors") for each adapter."""
    neighbors = dict()
    joltage_increases = [1, 2, 3]

    for adapter in adapters:
        potential_neighbors = [adapter + num for num in joltage_increases]
        neighbors[adapter] = \
            [neighbor for neighbor in potential_neighbors if neighbor in adapters]

    return neighbors


def jolt_arrangements():
    """Get all possible adapter arrangments."""
    adapters = _load_adapters()
    charging_outlet = 0
    device = max(adapters) + 3
    data = [charging_outlet] + adapters + [device]
    neighbors = _get_neighbors(data)
    arrangements = _get_arrangement_counts(neighbors)
    return arrangements[device]

# print(jolt_arrangements())
