#!/usr/bin/env python3
import time

from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_red, right


def solve_puzzle_1() -> None:
    for i in range(11):
        forward()
        left(90)
        forward()
        right(90)


init_puzzle("levels/puzzle_1.png", x=-300, y=-250, speed=0)
solve_puzzle_1()
