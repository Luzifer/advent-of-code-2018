#!/usr/bin/env python
# -*- coding: utf-8 -*-

from timeit import default_timer as timer
import copy
import os
import uuid

DIR_LEFT = '<'
DIR_RIGHT = '>'
DIR_UP = '^'
DIR_DOWN = 'v'

TRACK_N_S = '|'
TRACK_W_E = '-'
TRACK_INTER = '+'
TRACK_CURVES = ['/', '\\']


class Cart:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.direction = d
        # Left (l) -> Straight (s) -> Right (r) -> Repeat
        self.turns = ['l', 's', 'r']

        self.uuid = str(uuid.uuid4())

    def __str__(self):
        return 'X={} Y={} D={}'.format(self.x, self.y, self.direction)

    def __repr__(self):
        return self.__str__()

    def has_crash(self, oc):
        return oc.x == self.x and oc.y == self.y and oc.uuid != self.uuid

    def move(self, tg):
        if self.direction == DIR_LEFT:
            self.x -= 1
        elif self.direction == DIR_RIGHT:
            self.x += 1
        elif self.direction == DIR_UP:
            self.y -= 1
        elif self.direction == DIR_DOWN:
            self.y += 1

        track = tg.get_track_at(self.x, self.y)
        assert track != ' ', 'Cart stepped off the track'

        if track in TRACK_CURVES:
            if self.direction == DIR_LEFT and track == '/':
                self.direction = DIR_DOWN
            elif self.direction == DIR_LEFT and track == '\\':
                self.direction = DIR_UP

            elif self.direction == DIR_RIGHT and track == '/':
                self.direction = DIR_UP
            elif self.direction == DIR_RIGHT and track == '\\':
                self.direction = DIR_DOWN

            elif self.direction == DIR_UP and track == '/':
                self.direction = DIR_RIGHT
            elif self.direction == DIR_UP and track == '\\':
                self.direction = DIR_LEFT

            elif self.direction == DIR_DOWN and track == '/':
                self.direction = DIR_LEFT
            elif self.direction == DIR_DOWN and track == '\\':
                self.direction = DIR_RIGHT
        elif track == TRACK_INTER:
            chg = self.turns[0]
            del self.turns[0]
            self.turns.append(chg)

            if chg == 'l' and self.direction == DIR_LEFT:
                self.direction = DIR_DOWN
            elif chg == 'l' and self.direction == DIR_RIGHT:
                self.direction = DIR_UP
            elif chg == 'l' and self.direction == DIR_UP:
                self.direction = DIR_LEFT
            elif chg == 'l' and self.direction == DIR_DOWN:
                self.direction = DIR_RIGHT

            elif chg == 'r' and self.direction == DIR_LEFT:
                self.direction = DIR_UP
            elif chg == 'r' and self.direction == DIR_RIGHT:
                self.direction = DIR_DOWN
            elif chg == 'r' and self.direction == DIR_UP:
                self.direction = DIR_RIGHT
            elif chg == 'r' and self.direction == DIR_DOWN:
                self.direction = DIR_LEFT


class TrackGrid:
    def __init__(self, f):
        self.grid = []
        self.carts = []

        row = []
        for line in f:
            for c in line.strip('\n'):
                if c in [DIR_LEFT, DIR_RIGHT, DIR_UP, DIR_DOWN]:
                    # We have a cart
                    self.carts.append(Cart(len(row), len(self.grid), c))
                    if c in [DIR_LEFT, DIR_RIGHT]:
                        c = TRACK_W_E
                    elif c in [DIR_UP, DIR_DOWN]:
                        c = TRACK_N_S
                row.append(c)
            self.grid.append(row)
            row = []

    def get_track_at(self, x, y):
        return self.grid[y][x]

    def print(self, display_cart=True):
        tmp_grid = copy.deepcopy(self.grid)
        if display_cart:
            for cart in self.carts:
                tmp_grid[cart.y][cart.x] = cart.direction

        for row in tmp_grid:
            print(''.join(row))

    def tick(self):
        collisions = []
        broken = []

        for cart in sorted(self.carts, key=lambda c: [c.y, c.x]):
            cart.move(self)

            for oc in self.carts:
                if cart.has_crash(oc):
                    collisions.append([cart.x, cart.y])
                    broken.append(cart)
                    broken.append(oc)

        for cart in broken:
            self.carts.remove(cart)

        return collisions, len(self.carts)


def ingest_data():
    data_file = 'data/{}.txt'.format(
        os.path.basename(__file__).strip('.py'),
    )

    indata = None
    with open(data_file) as f:
        indata = TrackGrid(f)

    return indata


def solve_problem1(indata):
    tg = copy.deepcopy(indata)
    for i in range(0, 1000000):
        collisions, remaining = tg.tick()
        if len(collisions) > 0:
            return '{},{}'.format(*collisions[0])


def solve_problem2(indata):
    tg = copy.deepcopy(indata)
    for i in range(0, 1000000):
        collisions, remaining = tg.tick()
        if remaining == 1:
            return '{},{}'.format(tg.carts[0].x, tg.carts[0].y)


def tests():
    test_grid = TrackGrid(['/->-\        ',
                           '|   |  /----\\',
                           '| /-+--+-\  |',
                           '| | |  | v  |',
                           '\-+-/  \-+--/',
                           '  \------/   '])

    collided = False
    for i in range(0, 100):
        collisions, remaining = test_grid.tick()
        if len(collisions) > 0:
            assert collisions[0] == [7, 3], \
                'Test grid has wrong collision coordinates ({},{})'.format(
                    *collisions[0])
            collided = True
            break

    assert collided, 'No collision was recorded'


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
