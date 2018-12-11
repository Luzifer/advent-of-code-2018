#!/usr/bin/env python
# -*- coding: utf-8 -*-

from timeit import default_timer as timer
import os


def ingest_data():
    data_file = 'data/{}.txt'.format(
        os.path.basename(__file__).strip('.py'),
    )

    indata = ""
    with open(data_file) as f:
        indata = f.read().strip()

    return indata


def solve_problem1(indata):
    pass


def solve_problem2(indata):
    pass


def tests():
    pass


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
