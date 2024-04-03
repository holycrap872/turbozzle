#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_red, right, wait_until_exit


def solve_puzzle_2():
    forward()
    if on_red():
        right(90)
    solve_puzzle_2()


init_puzzle("levels/puzzle_2.png", x=-300, y=-250, speed=3)
solve_puzzle_2()

wait_until_exit()
