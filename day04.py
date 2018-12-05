#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def get_sleep_matrix(events):
    guardsleep = {}

    awake = True
    guard = -1  # Nobody
    minute = 0
    for event in events:
        if event['guard'] != guard:
            # Guard switched
            guard = event['guard']
            awake = True  # Guard is awake when going on duty
            minute = 0
            if event['guard'] not in guardsleep:
                guardsleep[event['guard']] = [0 for i in range(0, 60)]

        awake = event['awake']
        if awake:
            for m in range(minute, event['minute']):
                guardsleep[event['guard']][m] += 1
        minute = event['minute']

    return guardsleep


def solve_problem1(events):
    guardsleep = get_sleep_matrix(events)

    most_asleep = -1
    asleep_minutes = 0
    for guard, sleep in guardsleep.items():
        if sum(sleep) > asleep_minutes:
            most_asleep = guard
            asleep_minutes = sum(sleep)

    print('Most={} Minutes={} Max={} Idx={}'.format(
        most_asleep,
        asleep_minutes,
        max(guardsleep[most_asleep]),
        guardsleep[most_asleep].index(max(guardsleep[most_asleep])),
    ))

    return most_asleep * guardsleep[most_asleep].index(max(guardsleep[most_asleep]))


def solve_problem2(events):
    guardsleep = get_sleep_matrix(events)

    most_asleep = -1
    max_freq_asleep = 0
    for guard, sleep in guardsleep.items():
        if max(sleep) > max_freq_asleep:
            most_asleep = guard
            max_freq_asleep = max(sleep)

    print('Most={} Freq={} Max={} Idx={}'.format(
        most_asleep,
        max_freq_asleep,
        max(guardsleep[most_asleep]),
        guardsleep[most_asleep].index(max(guardsleep[most_asleep])),
    ))

    return most_asleep * guardsleep[most_asleep].index(max(guardsleep[most_asleep]))


def main():
    events = []
    with open('data/day04.txt') as f:
        guard = None
        for line in sorted(f.read().strip().split('\n')):
            shiftbegin = re.search(r'Guard #([0-9]+) begins shift', line)
            if shiftbegin is not None:
                guard = shiftbegin.group(1)
                continue
            awake = ('falls asleep' not in line)
            t = re.search(r'\[.*:([0-9]{2})\]', line)
            if t == None:
                raise Exception('Invalid line: {}'.format(line))
            events.append({
                'guard': int(guard),
                'minute': int(t.group(1)),
                'awake': awake,
            })

    print('Solution part 1: {}'.format(solve_problem1(events)))
    print('Solution part 2: {}'.format(solve_problem2(events)))


if __name__ == '__main__':
    main()
