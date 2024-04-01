#!/usr/bin/env python3
import time

from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_red, right


def solve_puzzle_0() -> None:
    for i in range(10):
        if on_red():
            left(90)
        forward()


init_puzzle("levels/puzzle_0.png", x=-250, y=0, speed=1)
solve_puzzle_0()
