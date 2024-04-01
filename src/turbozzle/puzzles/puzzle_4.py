#!/usr/bin/env python3
import time

from turbozzle.utils.movement_wrapper import (
    forward,
    init_puzzle,
    left,
    on_purple,
    on_red,
    right,
)


def solve_puzzle_4() -> None:
    forward()
    if on_red():
        left(90)
    if on_purple():
        right(90)

    solve_puzzle_4()


init_puzzle("levels/puzzle_4.png", x=-300, y=-300, speed=0)
solve_puzzle_4()
