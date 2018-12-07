#!/usr/bin/env python
# -*- coding: utf-8 -*-


def all_in(l, s):
    for c in l:
        if c not in s:
            return False
    return True


def get_next(indata, done, assigned=[]):
    keys = sorted(indata.keys())

    for k in keys:
        if k in done:
            continue

        if k in assigned:
            continue

        if len(indata[k]) > 0 and not all_in(indata[k], done):
            continue

        return k

    return None


def solve_problem1(indata):
    output = ''

    while len(output) < len(indata):
        output = ''.join([output, get_next(indata, output)])

    return output


def solve_problem2(indata):
    done = []
    assigned = []

    workers = [
        [None, 0],  # Task, Remaining seconds
        [None, 0],
        [None, 0],
        [None, 0],
        [None, 0],
    ]

    current_time = 0
    while len(done) < len(indata):
        # See state of current tasks
        for i in range(0, len(workers)):
            if workers[i][0] is not None:
                workers[i][1] -= 1  # One second has passed
                if workers[i][1] == 0:
                    done.append(workers[i][0])
                    assigned.remove(workers[i][0])
                    workers[i][0] = None

            if workers[i][0] is None:
                nt = get_next(indata, done, assigned)
                if nt is not None:
                    assigned.append(nt)
                    workers[i][0] = nt
                    workers[i][1] = 60 + (ord(nt) - 64)

        current_time += 1

    return current_time-1


def main():
    indata = {}
    with open('data/day07.txt') as f:
        for line in f:
            parts = line.strip().split(' ')
            if len(parts) == 0:
                continue
            parent = parts[1]
            leaf = parts[7]

            for c in [parent, leaf]:
                if c not in indata:
                    indata[c] = []

            indata[leaf].append(parent)

    print('Solution part 1: {}'.format(solve_problem1(indata)))
    print('Solution part 2: {}'.format(solve_problem2(indata)))


if __name__ == '__main__':
    main()
