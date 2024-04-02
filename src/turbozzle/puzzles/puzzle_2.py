#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_red, right


def solve_puzzle_2() -> None:
    forward()
    if on_red():
        left(90)
    solve_puzzle_2()


init_puzzle("levels/puzzle_2.png", x=-300, y=-250, speed=2)
solve_puzzle_2()
