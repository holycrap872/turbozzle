#! /usr/bin/env python3
import turtle

from turbozzle.creator.levels import (
    LEVEL_1,
    LEVEL_2,
    LEVEL_3,
    LEVEL_4,
    LEVEL_5,
    LEVEL_6,
    LEVEL_7,
    LEVEL_8,
    LEVEL_9,
    MY_LEVEL,
    get_color,
)


def draw_box(t: turtle.Turtle, color: str) -> None:
    """
    Draws a single 46x46 box of the specified color.
    :param t: Turtle that is used to draw
    :param color: Color to make the box
    """
    t.fillcolor(color)
    t.begin_fill()

    t.pendown()
    t.pensize(2)
    for _ in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()
    t.penup()


def draw_row(t: turtle.Turtle, colors: list[str], y_value: int) -> None:
    """
    Draws a horizontal line of boxes based on the list of colors.
    """
    t.speed(0)

    start_x = -(len(colors) * 50) / 2  # Center boxes
    t.goto(start_x, y_value)

    for color_code in colors:
        color = get_color(color_code)
        draw_box(t, color)
        t.forward(50)  # Move to the position for the next box


def draw_level(level: list[list[str]]) -> None:
    screen = turtle.Screen()
    screen.title("Color Boxes")

    t = turtle.Turtle()
    t.penup()

    row_y = 300
    for row in level:
        draw_row(t, row, row_y)
        row_y = row_y - 50

    screen.mainloop()


draw_level(MY_LEVEL)
