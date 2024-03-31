#!/usr/bin/env python3
import os
import time
import turtle
import typing

from turbozzle.creator.levels import FILE_TO_LEVEL_MAP, get_color


class LevelConfig(typing.NamedTuple):
    file_name: str
    speed: int
    level_data: list[list[str]]


CONFIG_INFO: typing.Optional[LevelConfig] = None


def __handle_speed(config: LevelConfig) -> None:
    speed: int = config.speed
    if speed != 0:
        wait = (6 - speed) * 0.1
        time.sleep(wait)


def sample_color(config: LevelConfig, x: int, y: int) -> typing.Optional[str]:
    level_data = config.level_data

    box_size = 50
    num_rows = len(level_data)
    num_columns = len(level_data[0])

    total_width = num_columns * box_size
    total_height = num_rows * box_size

    relative_x = (total_width / 2) + x
    relative_y = (total_height / 2) - y

    # Calculate column and row indices
    if 0 <= relative_x < total_width:
        column_index = int(relative_x / box_size)
    else:
        return None  # Horizontally outside the grid

    if 0 <= relative_y < total_height:
        row_index = int(relative_y / box_size)
    else:
        return None  # Vertically outside the grid

    return get_color(level_data[row_index][column_index])


def init_maze(background_path: str, *, x: int, y: int, speed: int) -> None:
    global CONFIG_INFO

    file_name = os.path.basename(background_path)
    CONFIG_INFO = LevelConfig(file_name, speed, FILE_TO_LEVEL_MAP[file_name])

    turtle.bgpic(background_path)

    # bring the turtle to the starting point
    turtle.penup()
    turtle.clear()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.pensize(5)
    turtle.pencolor("red")
    turtle.speed(speed)


def forward(num_pixels: int) -> None:
    assert CONFIG_INFO

    __handle_speed(CONFIG_INFO)
    turtle.forward(num_pixels)


def left(degrees: int) -> None:
    assert CONFIG_INFO

    __handle_speed(CONFIG_INFO)
    turtle.left(degrees)


def right(degrees: int) -> None:
    assert CONFIG_INFO

    __handle_speed(CONFIG_INFO)
    turtle.right(degrees)


def _on_color(color: str) -> bool:
    assert CONFIG_INFO

    x, y = turtle.pos()
    return sample_color(CONFIG_INFO, int(x), int(y)) == color


def on_red() -> bool:
    return _on_color("red")


def on_green() -> bool:
    return _on_color("green")


def on_blue() -> bool:
    return _on_color("blue")


def on_yellow() -> bool:
    return _on_color("yellow")