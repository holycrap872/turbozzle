#!/usr/bin/env python3
import time

from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_red, right


def solve_puzzle_5() -> None:
    forward()
    left(90)
    forward()
    right(90)
    if on_red():
        right(90)
    solve_puzzle_5()


init_puzzle("levels/puzzle_5.png", x=-300, y=0, speed=0)
solve_puzzle_5()
