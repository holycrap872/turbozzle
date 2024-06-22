#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, right, wait_until_exit


def solve_puzzle_03():
    for i in range(8):
        "CAN REPLACE"
        "CAN REPLACE"
        "CAN REPLACE"
        "CAN REPLACE"


init_puzzle("levels/puzzle_03.png", x=-300, y=-250, speed=0)
solve_puzzle_03()

wait_until_exit()
