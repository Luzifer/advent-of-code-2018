#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def react_polymer(line):
    reductions = []
    for i in range(ord('A'), ord('Z')+1):
        reductions.append('{}{}'.format(chr(i), chr(i+32)))
        reductions.append('{}{}'.format(chr(i+32), chr(i)))

    repl = r'({})'.format('|'.join(reductions))

    l = len(line)
    while True:
        line = re.sub(repl, '', line)
        if len(line) == l:
            break
        l = len(line)

    return line


def solve_problem1(line):
    return len(react_polymer(line))


def solve_problem2(line):
    shortest = len(line)  # Nothing can be bigger, use as MaxINT

    for i in range(ord('A'), ord('Z')+1):
        repl = r'[{}{}]'.format(chr(i), chr(i+32))

        l = len(react_polymer(re.sub(repl, '', line)))
        if l < shortest:
            shortest = l

    return shortest


def main():
    line = ""
    with open('data/day05.txt') as f:
        line = f.read().strip()

    print('Solution part 1: {}'.format(solve_problem1(line)))
    print('Solution part 2: {}'.format(solve_problem2(line)))


if __name__ == '__main__':
    main()
