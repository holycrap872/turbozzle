#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, right, wait_until_exit


def solve_puzzle_8() -> None:

    right(90)
    for i in range(1, 11):
        for _ in range(i):
            forward()
        right(90)


init_puzzle("levels/puzzle_8.png", x=50, y=0, speed=0)
solve_puzzle_8()

wait_until_exit()
