#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_purple, on_red, right, wait_until_exit


def solve_puzzle_05() -> None:
    left(90)
    while True:
        forward()
        if on_red():
            right(90)
        if on_purple():
            left(90)


init_puzzle("levels/puzzle_05.png", x=0, y=-250, speed=0)
solve_puzzle_05()

wait_until_exit()
