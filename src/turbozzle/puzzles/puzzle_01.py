#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, wait_until_exit


def do_something_1():
    forward()
    forward()
    left(90)


def do_something_2():
    forward()
    forward()
    forward()
    forward()
    forward()


def solve_puzzle_01():
    left(180)

    for i in range(2):
        do_something_1()

    for i in range(2):
        do_something_2()
        left(90)


init_puzzle("levels/puzzle_01.png", x=0, y=0, speed=3)
solve_puzzle_01()

wait_until_exit()
