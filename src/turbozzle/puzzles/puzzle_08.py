#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_red, right, wait_until_exit


def solve_puzzle_08() -> None:
    forward()
    left(90)
    forward()
    right(90)
    if on_red():
        right(90)
    solve_puzzle_08()


init_puzzle("levels/puzzle_08.png", x=-300, y=0, speed=0)
solve_puzzle_08()

wait_until_exit()
