#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, wait_until_exit


def solve_puzzle_4() -> None:

    for i in range(5):
        for i in range(2):
            forward()
        left(90)
        for i in range(7):
            forward()
        left(180)
        for i in range(7):
            forward()
        left(90)


init_puzzle("levels/puzzle_4.png", x=-250, y=-200, speed=0)
solve_puzzle_4()

wait_until_exit()
