#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_red, right, wait_until_exit


def solve_puzzle_09() -> None:
    "YOUR CODE HERE"


init_puzzle("levels/puzzle_09.png", x=0, y=0, speed=0)
solve_puzzle_09()

wait_until_exit()
