#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, right, wait_until_exit


def move_forward_1():
    forward()


def move_forward_3_and_turn():
    for i in range(3):
        forward()
    left(90)


def move_forward_4():
    for i in range(4):
        forward()


def solve_puzzle_04():
    for i in range(4):
        move_forward_4()
        move_forward_1()
        move_forward_3_and_turn()


init_puzzle("levels/puzzle_04.png", x=-200, y=-200, speed=0)
solve_puzzle_04()

wait_until_exit()
