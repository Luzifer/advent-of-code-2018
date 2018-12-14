#!/usr/bin/env python
# -*- coding: utf-8 -*-

from timeit import default_timer as timer
import math
import os


def fill_len_x(indata, x, match=None):
    data = [indata[i] if i < len(indata) else 0 for i in range(0, x)]
    p1 = 0
    p2 = 1
    l = len(indata)

    while l < x:
        s = data[p1] + data[p2]
        for i in [int(i) for i in str(s)]:
            if l >= len(data):
                break
            data[l] = i
            l += 1

        p1 = p1 + 1+data[p1]
        p1 -= int(math.floor(p1 / l)*l)

        p2 = p2 + 1+data[p2]
        p2 -= int(math.floor(p2 / l)*l)

    if match is not None:
        for i in range(l-len(match)):
            if data[i:i+len(match)] == match:
                return data, i

    return data, -1


def ingest_data():
    data_file = 'data/{}.txt'.format(
        os.path.basename(__file__).strip('.py'),
    )

    indata = 0
    with open(data_file) as f:
        indata = int(f.read().strip())

    return indata


def solve_problem1(indata):
    data, n = fill_len_x([3, 7], indata+10)
    return ''.join([str(i) for i in data[indata:indata+10]])


def solve_problem2(indata):
    for p in range(4, 10):
        data, n = fill_len_x([3, 7], 10**p, [int(i) for i in str(indata)])
        if n > -1:
            return n


def tests():
    data, n = fill_len_x([3, 7], 20)
    assert data == [3, 7, 1, 0, 1, 0, 1, 2, 4, 5, 1, 5, 8, 9, 1, 6, 7, 7, 9, 2]
    assert data[9: 19] == [5, 1, 5, 8, 9, 1, 6, 7, 7, 9]
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
