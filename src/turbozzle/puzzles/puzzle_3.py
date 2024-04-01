#!/usr/bin/env python3
import time

from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_red, right


def solve_puzzle_3() -> None:

    forward(50)
    for i in range(5):
        for i in range(2):
            forward(50)
        left(90)
        for i in range(7):
            forward(50)
        left(180)
        for i in range(7):
            forward(50)
        left(90)


init_puzzle("levels/puzzle_3.png", x=-300, y=-200, speed=0)
solve_puzzle_3()
