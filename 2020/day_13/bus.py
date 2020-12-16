"""Bus module."""

import os
import json


SCHEDULE_JSON = 'schedule.json'


def earliest_bus():
    """Find earliest bus."""
    data = _load_schedule()

    buses = [bus_id for bus_id in data['bus_ids'] if not bus_id == 'x']
    timestamp = data['timestamp']
    bus_times = {}

    for bus in buses:
        quotient = int(timestamp / bus)
        bus_time = bus * quotient
        if bus_time < timestamp:
            bus_time = bus * (quotient + 1)
        bus_times[bus] = bus_time

    filtered_buses = {bus: time for bus, time in bus_times.items() if time > timestamp}
    soonest_time = min(filtered_buses.values())
    wait_time = soonest_time - timestamp
    bus_num = [bus for bus, time in filtered_buses.items() if time == soonest_time][0]

    print(f'BUS: {bus_num}, TIME: {soonest_time}, WAIT: {wait_time}')
    return bus_num * wait_time


def sequential_buses():
    """Earliest time buses will depart sequentially using chinese remainder theorem."""
    data = _load_schedule()
    mod_tuples = _mods(data.get('bus_ids'))

    coefficient = 1
    remainder = 0

    for pair in mod_tuples:
        mod = pair[0]
        bus_id = pair[1]

        for i in range(1, bus_id):
            if coefficient * i % bus_id == 1:
                new_r = (((mod - remainder) * i) % bus_id) * coefficient + remainder
                new_c = coefficient * bus_id
                remainder = new_r
                coefficient = new_c
                break

    return remainder


def _load_schedule():
    """Load schedule json."""
    filepath = os.path.join(os.getcwd(), os.path.dirname(__file__), SCHEDULE_JSON)
    f = open(filepath, 'r')
    schedule = json.load(f)
    f.close()
    return schedule


def _mods(bus_ids: list):
    """Get modular equations for each bus_id in list."""
    mods_list = list()

    for i in range(len(bus_ids)):
        bus_id = bus_ids[i]
        if not bus_id == 'x':
            mods_list.append((-i % bus_id, bus_id))

    return mods_list


# SOLUTION 1 | 2045
# earliest_bus()


# SOLUTION 2 | 402251700208309
# print(sequential_buses())
