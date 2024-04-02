#!/usr/bin/env python3
import time

from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_red, right


def solve_puzzle_8() -> None:

    for i in range(10, 0, -1):
        for _ in range(i):
            forward()
        left(90)


init_puzzle("levels/puzzle_8.png", x=-250, y=-250, speed=0)
solve_puzzle_8()
