#!/usr/bin/env python
# -*- coding: utf-8 -*-

MAXINT = 2**31 - 1


def get_max_n(coords, n):
    m = 0
    for c in coords:
        if c[n] > m:
            m = c[n]
    return m


def get_nearest(coords, fx, fy):
    coord = None
    dists = [MAXINT]
    for (x, y) in coords:
        cdist = manhatten(x, y, fx, fy)
        if cdist < min(dists):
            coord = (x, y)
        dists.append(cdist)

    if dists.count(min(dists)) > 1:
        return -1

    return coords.index(coord)


def get_sum_dist(coords, fx, fy):
    total_dist = 0

    for (x, y) in coords:
        total_dist += manhatten(x, y, fx, fy)

    return total_dist


def is_infinite(coords, coord):
    (x, y) = coords[coord]

    return get_nearest(coords, x-10000, y) == coord or \
        get_nearest(coords, x+10000, y) == coord or \
        get_nearest(coords, x, y-10000) == coord or \
        get_nearest(coords, x, y+10000) == coord or \
        get_nearest(coords, -10000, -10000) == coord or \
        get_nearest(coords, 10000, -10000) == coord or \
        get_nearest(coords, -10000, 10000) == coord or \
        get_nearest(coords, 10000, 10000) == coord


def manhatten(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def solve_problem1(coords):
    field = [[get_nearest(coords, x, y)
              for x in range(0, get_max_n(coords, 0)+2)]
             for y in range(0, get_max_n(coords, 1)+2)]

    area = 0
    coord = -1

    for i in range(0, len(coords)):
        if is_infinite(coords, i):
            continue

        ia = sum([y.count(i) for y in field])
        if ia > area:
            area = ia
            coord = i

    return area


def solve_problem2(coords):
    field = [[1 if get_sum_dist(coords, x, y) < 10000 else 0
              for x in range(0, get_max_n(coords, 0)+2)]
             for y in range(0, get_max_n(coords, 1)+2)]

    return sum([sum(row) for row in field])


def main():
    coords = []
    with open('data/day06.txt') as f:
        for line in f:
            (x, y) = line.split(', ')
            coords.append((int(x), int(y)))

    print('Solution part 1: {}'.format(solve_problem1(coords)))
    print('Solution part 2: {}'.format(solve_problem2(coords)))


if __name__ == '__main__':
    main()
