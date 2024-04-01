#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_red, right


def solve_puzzle_2() -> None:
    for i in range(11):
        forward()
        left(90)
        forward()
        right(90)


init_puzzle("levels/puzzle_2.png", x=-300, y=-250, speed=0)
solve_puzzle_2()
