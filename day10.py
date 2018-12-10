#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def graph_pts(pts):
    px = [e[0] for e in pts]
    py = [e[1] for e in pts]

    field = [['\u2591' for x in range(min(px), max(px)+1)]
             for y in range(min(py), max(py)+1)]

    for p in pts:
        field[p[1]-min(py)][p[0]-min(px)] = '\u2593'

    for x in field:
        print(''.join(x))


def solve_problem1(indata):
    return 'See print below'


def solve_problem2(indata):
    min_bb = 2**31-1  # replacement for maxint
    snap = None

    for c in range(0, 500000):
        pts = [[e[0]+e[2]*c, e[1]+e[3]*c] for e in indata]
        x = [e[0] for e in pts]
        y = [e[1] for e in pts]

        w = max(x) - min(x)
        h = max(y) - min(y)

        if w*h < min_bb:
            min_bb = w*h
            snap = c

    graph_pts([[e[0]+e[2]*snap, e[1]+e[3]*snap] for e in indata])

    return snap


def main():
    indata = []
    with open('data/day10.txt') as f:
        for line in f:
            coords = [int(e) for e in re.findall(r'[0-9-]+', line)]
            assert len(coords) == 4
            indata.append(coords)

    print('Solution part 1: {}'.format(solve_problem1(indata)))
    print('Solution part 2: {}'.format(solve_problem2(indata)))


if __name__ == '__main__':
    main()
