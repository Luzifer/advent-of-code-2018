#!/usr/bin/env python
# -*- coding: utf-8 -*-

import difflib


def get_multi_letter_counts(box_ids):
    n2, n3 = {}, {}

    for box_id in box_ids:
        char_counts = {s: list(box_id).count(s) for s in list(box_id)}

        for c, n in char_counts.items():
            if n == 2:
                n2[box_id] = True
            elif n == 3:
                n3[box_id] = True

    return (len(n2), len(n3))


def find_close_two(box_ids):
    for b1 in box_ids:
        for b2 in box_ids:
            diffs = 0
            diff_idx = -1

            for i, s in enumerate(difflib.ndiff(b1, b2)):
                if s[0] == '':
                    continue
                if s[0] == '-':
                    diffs += 1
                    diff_idx = i

            if diffs == 1:
                box_id = list(b1)
                del box_id[diff_idx]
                return ''.join(box_id)

    raise Exception("No matches found")


def main():
    box_ids = []
    with open('day02.txt') as f:
        for line in f:
            box_ids.append(line.strip())

    (n2, n3) = get_multi_letter_counts(box_ids)
    print('Solution part 1: {}'.format(n2*n3))

    print('Solution part 2: {}'.format(find_close_two(box_ids)))


if __name__ == '__main__':
    main()
