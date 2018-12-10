#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import deque


def get_highscore(indata):
    circle = deque('0')
    current_player = 0

    player_scores = [0 for i in range(0, indata[0]+1)]

    for i in range(1, indata[1]+1):
        # Pass to next player, start at beginning on last player
        current_player += 1
        if current_player > indata[0]:
            current_player = 1

        # Handle mod-23 exception of the rule
        if i % 23 == 0:
            player_scores[current_player] += i
            circle.rotate(-7)
            player_scores[current_player] += circle.pop()
            continue

        # Insert the marble according to insertion rule
        circle.rotate(2)
        circle.append(i)

    return max(player_scores)


def parse_input(txt):
    res = re.search(
        r'^([0-9]+) players; last marble is worth ([0-9]+) points$', txt)

    if res is None:
        raise Exception('Invalid input found')

    return (int(res.group(1)), int(res.group(2)))


def solve_problem1(indata):
    return get_highscore(indata)


def solve_problem2(indata):
    return get_highscore((indata[0], indata[1]*100))


def test_get_highscore():
    # Test cases defined in the question text
    assert get_highscore((9, 25)) == 32
    assert get_highscore((10, 1618)) == 8317
    assert get_highscore((13, 7999)) == 146373
    assert get_highscore((17, 1104)) == 2764
    assert get_highscore((21, 6111)) == 54718
    assert get_highscore((30, 5809)) == 37305


def main():
    test_get_highscore()

    indata = ()
    with open('data/day09.txt') as f:
        indata = parse_input(f.read().strip())

    print('Solution part 1: {}'.format(solve_problem1(indata)))
    print('Solution part 2: {}'.format(solve_problem2(indata)))


if __name__ == '__main__':
    main()
