#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_purple, on_red, right, wait_until_exit


def solve_puzzle_05() -> None:
    while True:
        forward()
        if on_red():
            right(90)
        if on_purple():
            left(90)


init_puzzle("levels/puzzle_05.png", x=-250, y=0, speed=2)
solve_puzzle_05()

wait_until_exit()
