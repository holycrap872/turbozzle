#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, wait_until_exit


def go_two_spaces_then_turn():
    forward()
    forward()
    left(90)


def go_five_spaces_then_turn():
    forward()
    forward()
    forward()
    forward()
    forward()


def solve_puzzle_01() -> None:
    for i in range(2):
        go_two_spaces_then_turn()
    for i in range(3):
        go_five_spaces_then_turn()
        left(90)


init_puzzle("levels/puzzle_01.png", x=0, y=0, speed=3)
solve_puzzle_01()

wait_until_exit()
