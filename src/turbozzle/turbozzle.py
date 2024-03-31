#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import *


def solve_maze_0() -> None:
    init_maze("CourseMaterial/03_advanced_programming/06_python_mazes/examples/maze_0.png", x=-250, y=0, speed=1)

    for i in range(10):
        if on_red():
            left(90)
        forward(50)


def solve_maze_1() -> None:
    init_maze("CourseMaterial/03_advanced_programming/06_python_mazes/examples/maze_1.png", x=-300, y=-250, speed=0)

    for i in range(11):
        forward(50)
        left(90)
        forward(50)
        right(90)


def solve_maze_2() -> None:
    init_maze("CourseMaterial/03_advanced_programming/06_python_mazes/examples/maze_2.png", x=-300, y=-250, speed=0)

    for i in range(21):
        forward(50)
        if on_red():
            left(90)


def solve_maze_3() -> None:
    init_maze("CourseMaterial/03_advanced_programming/06_python_mazes/examples/maze_3.png", x=-300, y=-200, speed=0)

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


if __name__ == "__main__":
    # solve_maze_0()
    # solve_maze_1()
    # solve_maze_2()
    solve_maze_3()

    time.sleep(10)
