#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_purple, on_red, right, wait_until_exit


def solve_puzzle_5() -> None:
    forward()
    if on_red():
        left(90)
    if on_purple():
        right(90)

    solve_puzzle_5()


init_puzzle("levels/puzzle_5.png", x=-250, y=-250, speed=0)
solve_puzzle_5()

wait_until_exit()
