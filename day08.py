#!/usr/bin/env python
# -*- coding: utf-8 -*-


def meta_sum(node):
    s = sum(node['m'])

    for c in node['c']:
        s += meta_sum(c)

    return s


def node_value(node):
    if len(node['c']) == 0:
        return sum(node['m'])

    v = 0

    for m in node['m']:
        if m-1 >= len(node['c']) or m == 0:
            continue
        v += node_value(node['c'][m-1])

    return v


def read_node(nums, idx):
    no_nodes = nums[idx]
    no_meta = nums[idx+1]

    children = []
    meta = []

    idx += 2
    for i in range(0, no_nodes):
        n, idx = read_node(nums, idx)
        children.append(n)

    for i in range(0, no_meta):
        meta.append(nums[idx])
        idx += 1

    return {'c': children, 'm': meta}, idx


def solve_problem1(indata):
    return meta_sum(indata)


def solve_problem2(indata):
    return node_value(indata)


def main():
    indata = None
    with open('data/day08.txt') as f:
        nums = [int(i) for i in f.read().strip().split(' ')]
        indata, idx = read_node(nums, 0)

        assert idx == len(nums)

    print('Solution part 1: {}'.format(solve_problem1(indata)))
    print('Solution part 2: {}'.format(solve_problem2(indata)))


if __name__ == '__main__':
    main()
