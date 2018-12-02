#!/usr/bin/env python
# -*- coding: utf-8 -*-


def loop_until_duplicate(numbers):
    encounters = [0]
    state = 0
    loops = 0
    while True:
        for n in numbers:
            state += n

            if state in encounters:
                return state

            encounters.append(state)

        loops += 1
        if loops % 1000 == 0:
            print('Loops: {}'.format(loops))


def main():
    numbers = []
    with open('data/day01.txt') as f:
        for line in f:
            numbers.append(int(line))

    print('Solution part 1: {}'.format(sum(numbers)))

    print('Solution part 2: {}'.format(loop_until_duplicate(numbers)))


if __name__ == '__main__':
    main()
