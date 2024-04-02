#!/usr/bin/env python3
import time

from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_red, right


def solve_puzzle_7() -> None:
    for i in range(4):
        for i in range(5):
            forward()
        left(180)
        for i in range(5):
            forward()
        left(90)


init_puzzle("levels/puzzle_7.png", x=0, y=0, speed=0)
solve_puzzle_7()
time.sleep(10)
