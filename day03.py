#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def get_overlapping_area(claims):
    w, h = 0, 0

    for claim in claims:
        if claim['x']+claim['w'] > w:
            w = claim['x']+claim['w']
        if claim['y']+claim['h'] > h:
            h = claim['y']+claim['h']

    material = [[0 for x in range(w)] for y in range(h)]

    for claim in claims:
        for x in range(claim['x'], claim['x']+claim['w']):
            for y in range(claim['y'], claim['y']+claim['h']):
                material[y][x] += 1

    return material


def get_overlapping_sqin(claims):
    material = get_overlapping_area(claims)

    overlapping = 0
    for y in material:
        for x in y:
            if x > 1:
                overlapping += 1

    return overlapping


def get_non_overlapping_claim(claims):
    material = get_overlapping_area(claims)

    for claim in claims:
        overlaps = False

        for x in range(claim['x'], claim['x']+claim['w']):
            for y in range(claim['y'], claim['y']+claim['h']):
                if material[y][x] > 1:
                    overlaps = True

        if not overlaps:
            return claim


def main():
    claims = []
    claimre = re.compile(r'^#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)$')
    with open('data/day03.txt') as f:
        for line in f:
            m = claimre.search(line.strip())
            if m == None:
                raise Exception('Invalid claim: {}'.format(line))
            claims.append({
                'id': int(m.group(1)),
                'x': int(m.group(2)),
                'y': int(m.group(3)),
                'w': int(m.group(4)),
                'h': int(m.group(5)),
            })

    print('Solution part 1: {}'.format(get_overlapping_sqin(claims)))
    print('Solution part 2: {}'.format(
        get_non_overlapping_claim(claims)['id']))


if __name__ == '__main__':
    main()
