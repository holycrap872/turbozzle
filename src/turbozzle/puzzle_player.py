#!/usr/bin/env python3
import time

from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_red, right


def solve_puzzle_0() -> None:
    init_puzzle("levels/puzzle_0.png", x=-250, y=0, speed=1)

    for i in range(10):
        if on_red():
            left(90)
        forward(50)


def solve_puzzle_1() -> None:
    init_puzzle("levels/puzzle_1.png", x=-300, y=-250, speed=0)

    for i in range(11):
        forward(50)
        left(90)
        forward(50)
        right(90)


def solve_puzzle_2() -> None:
    init_puzzle("levels/puzzle_2.png", x=-300, y=-250, speed=0)

    for i in range(21):
        forward(50)
        if on_red():
            left(90)


def solve_puzzle_3() -> None:
    init_puzzle("levels/puzzle_3.png", x=-300, y=-200, speed=0)

    forward(50)
    for i in range(5):
        for i in range(2):
            forward(50)
        left(90)
        for i in range(7):
            forward(50)
        left(180)
        for i in range(7):
            forward(50)
        left(90)


def solve_puzzle_6() -> None:
    init_puzzle("levels/puzzle_6.png", x=-250, y=-250, speed=0)

    for i in range(10, 0, -1):
        for _ in range(i):
            forward(50)
        left(90)


if __name__ == "__main__":
    # solve_puzzle_0()
    # solve_puzzle_1()
    # solve_puzzle_2()
    # solve_puzzle_3()
    solve_puzzle_6()

    time.sleep(10)
