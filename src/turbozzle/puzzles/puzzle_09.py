#!/usr/bin/env python3
import time

from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_red, right, wait_until_exit


def solve_puzzle_09() -> None:
    for i in range(4):
        for i in range(5):
            forward()
        left(180)
        for i in range(5):
            forward()
        left(90)


init_puzzle("levels/puzzle_09.png", x=0, y=0, speed=0)
solve_puzzle_09()
time.sleep(10)

wait_until_exit()
