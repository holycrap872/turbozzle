#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import forward, init_puzzle, wait_until_exit


def solve_puzzle_00():
    for i in range(9):
        forward()


init_puzzle("levels/puzzle_00.png", x=-250, y=0, speed=3)
solve_puzzle_00()

wait_until_exit()
