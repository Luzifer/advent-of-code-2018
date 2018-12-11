#!/usr/bin/env python
# -*- coding: utf-8 -*-

from timeit import default_timer as timer
from functools import lru_cache
import os
import sys


def cell_power(x, y, serial):
    rack = x+10
    level = ((rack*y)+serial)*rack

    hd = 0
    if len(str(level)) >= 3:
        hd = int(str(level)[-3])

    return hd - 5


@lru_cache(maxsize=None)
def generate_grid(serial):
    grid = [[cell_power(x, y, serial) for x in range(0, 300)]
            for y in range(0, 300)]

    return grid


@lru_cache(maxsize=None)
def get_NxN_power(serial, tlx, tly, n=3):
    grid = generate_grid(serial)
    s = 0

    # Try to find the biggest factor to re-use previous calculations
    lf = largest_factor(n)
    if lf is not None and int(n/lf) != n:
        frag_n = int(n/lf)
        for x in range(0, frag_n):
            for y in range(0, frag_n):
                s += get_NxN_power(serial, tlx+x*lf,
                                   tly+y*lf, lf)
    else:
        for y in range(tly, tly+n):
            s += sum(grid[y][tlx:tlx+n])

    return s


def largest_factor(n):
    largest = None

    for i in range(1, n):
        if n % i == 0:
            largest = i

    return largest


def ingest_data():
    data_file = 'data/{}.txt'.format(
        os.path.basename(__file__).strip('.py'),
    )

    indata = None
    with open(data_file) as f:
        indata = int(f.read().strip())

    return indata


def solve_problem1(indata):
    max_power = 0
    coord = None

    for x in range(0, 298):
        for y in range(0, 298):
            power = get_NxN_power(indata, x, y)
            if power > max_power:
                max_power = power
                coord = [x, y]

    return ','.join([str(i) for i in coord])


def solve_problem2(indata):
    max_power = 0
    coord = None

    for n in range(1, 300):
        for x in range(0, 301-n):
            for y in range(0, 301-n):
                power = get_NxN_power(indata, x, y, n)
                if power > max_power:
                    max_power = power
                    coord = [x, y, n]

        # Draw some kind of progress bar
        sys.stdout.write('.')
        sys.stdout.flush()
    print('')

    return ','.join([str(i) for i in coord])


def test_cell_power():
    assert cell_power(3, 5, 8) == 4
    assert cell_power(122, 79, 57) == -5
    assert cell_power(217, 196, 39) == 0
    assert cell_power(101, 153, 71) == 4


def test_get_NxN_power():
    assert get_NxN_power(18, 33, 45) == 29
    assert get_NxN_power(42, 21, 61) == 30


def tests():
    test_cell_power()
    test_get_NxN_power()


def main():
    start = timer()
    tests()
    test = timer()

    indata = ingest_data()
    ingest = timer()

    print('Solution part 1: {}'.format(solve_problem1(indata)))
    s1 = timer()

    print('Solution part 2: {}'.format(solve_problem2(indata)))
    s2 = timer()

    print('\nExecution took {:.2f}s (Tests: {:.2f}s, Ingest: {:.2f}s, Solution 1; {:.2f}s, Solution 2: {:.2f}s)'.format(
        s2-start,
        test-start,
        ingest-test,
        s1-ingest,
        s2-s1,
    ))


if __name__ == '__main__':
    main()
