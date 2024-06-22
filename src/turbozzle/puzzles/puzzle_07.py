#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_purple, on_red, right, wait_until_exit


def solve_puzzle_07():
    "CAN REPLACE"
    "CAN REPLACE"

    if on_red():
        "CAN REPLACE"
        "CAN REPLACE"

    if on_purple():
        "CAN REPLACE"
        "CAN REPLACE"

    "CAN REPLACE"
    "CAN REPLACE"

    solve_puzzle_07()


init_puzzle("levels/puzzle_07.png", x="MUST_REPLACE", y="MUST_REPLACE", speed=0)
solve_puzzle_07()

wait_until_exit()
