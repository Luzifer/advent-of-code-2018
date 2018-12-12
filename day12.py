#!/usr/bin/env python
# -*- coding: utf-8 -*-

from timeit import default_timer as timer
import os
import sys


class RowOfPots:
    def __init__(self, state):
        self.buf = {}
        self.transaction = {}
        for i in range(0, len(state)):
            self.set(i, state[i])

    def commit(self):
        for x, v in self.transaction.items():
            self.set(x, v)
        self.transaction = {}

    def get(self, x):
        if x in self.buf:
            return self.buf[x]
        return '.'

    def get_centered(self, x, count=5):
        m = x-int((count-1)/2)
        lst = []
        for i in range(m, m+count):
            lst.append(self.get(i))

        return ''.join(lst)

    def get_row_display(self):
        lst = []
        for i in range(self.min(), self.max()+1):
            lst.append(self.get(i))
        return ''.join(lst)

    def max(self):
        return max(self.buf.keys())

    def min(self):
        return min(self.buf.keys())

    def prepare(self, x, v):
        self.transaction[x] = v

    def print(self):
        print(self.get_row_display())

    def set(self, x, v):
        if v == '.' and x in self.buf:
            del self.buf[x]
            return
        elif v == '#':
            self.buf[x] = v

    def sum_used_pots(self, shift=0):
        s = 0
        for k, v in self.buf.items():
            if v == '#':
                s += k+shift
        return s


def ingest_data():
    data_file = 'data/{}.txt'.format(
        os.path.basename(__file__).strip('.py'),
    )

    mutations = {}
    state = ""
    with open(data_file) as f:
        for line in f:
            if line.startswith('initial state'):
                state = line.strip().split(': ')[1]
                continue
            if '=>' in line:
                pattern, result = line.strip().split(' => ')
                mutations[pattern] = result

    return mutations, state


def solve_problem1(mutations, state):
    row = RowOfPots(state)

    for it in range(0, 20):
        for i in range(row.min()-5, row.max()+6):
            pots = row.get_centered(i)
            assert pots in mutations, 'Pot combination not found in muatations: {}'.format(
                pots)

            row.prepare(i, mutations[pots])
        row.commit()

    return row.sum_used_pots()


def solve_problem2(mutations, state):
    row = RowOfPots(state)

    display = None
    first_equal = 0
    conv_count = 0

    loop = 50000000000

    for it in range(0, loop):
        for i in range(row.min()-5, row.max()+6):
            pots = row.get_centered(i)
            assert pots in mutations, 'Pot combination not found in muatations: {}'.format(
                pots)

            row.prepare(i, mutations[pots])
        row.commit()

        if row.get_row_display() == display:
            conv_count += 1
        else:
            conv_count = 0
            display = row.get_row_display()
            first_equal = row.min()

        if conv_count == 10:
            # 10 iterations with same display
            shift = row.min() - first_equal

            # Use mathematics to prevent doing all shifts by calculating
            # the shift which will happen until the 50 billon iterations
            add = (loop - it-1) * int(shift/10)
            return row.sum_used_pots(add)

    return row.sum_used_pots()


def tests():
    pass


def main():
    start = timer()
    tests()
    test = timer()

    (mutations, state) = ingest_data()
    ingest = timer()

    print('Solution part 1: {}'.format(solve_problem1(mutations, state)))
    s1 = timer()

    print('Solution part 2: {}'.format(solve_problem2(mutations, state)))
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
