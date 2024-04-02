#!/usr/bin/env python3
import typing

_BLANK_LEVEL = [
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
]


LEVEL_1 = [
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "g", "b", "b", "b", "b", "y", "b", "b", "b", "b", "y", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
]


LEVEL_2 = [
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "y", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "b", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "b", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "b", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "b", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "b", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "b", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "b", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "b", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "b", "x"],
    ["g", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "r", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
]


LEVEL_3 = [
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "y", "b"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "b", "b", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "b", "b", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "b", "b", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "b", "b", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "b", "b", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "b", "b", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "b", "b", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "b", "b", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "b", "b", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "b", "b", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["g", "b", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
]


LEVEL_4 = [
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "y", "x", "y", "x", "y", "x", "y", "x", "y", "x"],
    ["x", "x", "x", "b", "x", "b", "x", "b", "x", "b", "x", "b", "x"],
    ["x", "x", "x", "b", "x", "b", "x", "b", "x", "b", "x", "b", "x"],
    ["x", "x", "x", "b", "x", "b", "x", "b", "x", "b", "x", "b", "x"],
    ["x", "x", "x", "b", "x", "b", "x", "b", "x", "b", "x", "b", "x"],
    ["x", "x", "x", "b", "x", "b", "x", "b", "x", "b", "x", "b", "x"],
    ["x", "x", "x", "b", "x", "b", "x", "b", "x", "b", "x", "b", "x"],
    ["g", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
]


LEVEL_5 = [
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "p", "b", "b", "b", "b", "b", "b", "b", "y", "b", "r", "x"],
    ["x", "p", "b", "y", "b", "b", "b", "b", "b", "b", "b", "r", "x"],
    ["x", "p", "b", "b", "b", "b", "b", "b", "b", "y", "b", "r", "x"],
    ["x", "p", "b", "y", "b", "b", "b", "b", "b", "b", "b", "r", "x"],
    ["x", "p", "b", "b", "b", "b", "b", "b", "b", "y", "b", "r", "x"],
    ["x", "p", "b", "y", "b", "b", "b", "b", "b", "b", "b", "r", "x"],
    ["x", "p", "b", "b", "b", "b", "b", "b", "b", "y", "b", "r", "x"],
    ["x", "p", "b", "y", "b", "b", "b", "b", "b", "b", "b", "r", "x"],
    ["x", "p", "b", "b", "b", "b", "b", "b", "b", "y", "b", "r", "x"],
    ["x", "p", "b", "y", "b", "b", "b", "b", "b", "b", "b", "r", "x"],
    ["x", "g", "b", "b", "b", "b", "b", "b", "b", "y", "b", "r", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
]


LEVEL_6 = [
    ["x", "x", "x", "x", "x", "x", "r", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "y", "b", "y", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "b", "b", "x", "b", "b", "x", "x", "x", "x"],
    ["x", "x", "x", "b", "b", "x", "x", "x", "b", "b", "x", "x", "x"],
    ["x", "x", "b", "b", "x", "x", "x", "x", "x", "b", "b", "x", "x"],
    ["x", "y", "b", "x", "x", "x", "x", "x", "x", "x", "b", "y", "x"],
    ["r", "b", "x", "x", "x", "x", "x", "x", "x", "x", "x", "b", "r"],
    ["x", "y", "b", "x", "x", "x", "x", "x", "x", "x", "b", "y", "x"],
    ["x", "x", "b", "b", "x", "x", "x", "x", "x", "b", "b", "x", "x"],
    ["x", "x", "x", "b", "b", "x", "x", "x", "b", "b", "x", "x", "x"],
    ["x", "x", "x", "x", "b", "b", "x", "b", "b", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "y", "b", "y", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "r", "x", "x", "x", "x", "x", "x"],
]


LEVEL_7 = [
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "y", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "b", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "b", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "b", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "b", "x", "x", "x", "x", "x", "x"],
    ["x", "y", "b", "b", "b", "b", "g", "b", "b", "b", "b", "y", "x"],
    ["x", "x", "x", "x", "x", "x", "b", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "b", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "b", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "b", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "y", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
]


LEVEL_8 = [
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "b", "b", "b", "b", "b", "b", "b", "b", "b", "x"],
    ["x", "x", "x", "b", "x", "x", "x", "x", "x", "x", "x", "b", "x"],
    ["x", "x", "x", "b", "x", "b", "b", "b", "b", "b", "x", "b", "x"],
    ["x", "x", "x", "b", "x", "b", "x", "x", "x", "b", "x", "b", "x"],
    ["x", "x", "x", "b", "x", "b", "x", "g", "x", "b", "x", "b", "x"],
    ["x", "x", "x", "b", "x", "b", "b", "b", "x", "b", "x", "b", "x"],
    ["x", "x", "x", "b", "x", "x", "x", "x", "x", "b", "x", "b", "x"],
    ["x", "x", "x", "b", "b", "b", "b", "b", "b", "b", "x", "b", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "b", "x"],
    ["x", "y", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
]


LEVEL_9 = [
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["y", "x", "x", "x", "y", "x", "x", "x", "y", "x", "x", "x", "y"],
    ["b", "b", "b", "b", "b", "x", "x", "x", "b", "b", "b", "b", "b"],
    ["y", "x", "b", "x", "y", "x", "x", "x", "y", "x", "b", "x", "y"],
    ["x", "x", "b", "x", "x", "x", "x", "x", "x", "x", "b", "x", "x"],
    ["x", "x", "b", "b", "b", "b", "b", "b", "b", "b", "b", "x", "x"],
    ["x", "x", "b", "x", "x", "x", "x", "x", "x", "x", "b", "x", "x"],
    ["y", "x", "b", "x", "y", "x", "x", "x", "y", "x", "b", "x", "y"],
    ["b", "b", "b", "b", "b", "x", "x", "x", "b", "b", "b", "b", "b"],
    ["y", "x", "x", "x", "y", "x", "x", "x", "y", "x", "x", "x", "y"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
]

COLOR_MAPPING = {
    "g": "green",
    "x": "black",
    "b": "blue",
    "y": "yellow",
    "r": "red",
    "p": "purple",
}


def get_color(color_code: str) -> str:
    return COLOR_MAPPING[color_code]


FILE_TO_LEVEL_MAP = {
    "puzzle_1.png": LEVEL_1,
    "puzzle_2.png": LEVEL_2,
    "puzzle_3.png": LEVEL_3,
    "puzzle_4.png": LEVEL_4,
    "puzzle_5.png": LEVEL_5,
    "puzzle_6.png": LEVEL_6,
    "puzzle_7.png": LEVEL_7,
    "puzzle_8.png": LEVEL_8,
    "puzzle_9.png": LEVEL_9,
}


class SquarePosition(typing.NamedTuple):
    row: int
    column: int


class LevelConfig:
    def __init__(self, file_name: str, speed: int, level_data: list[list[str]]) -> None:
        self.file_name = file_name
        self.speed = speed
        self.level_data = level_data
        self.goal_states: set[SquarePosition] = set()

        for row_index, row in enumerate(level_data):
            for column_index, val in enumerate(row):
                if val == "y":
                    self.goal_states.add(SquarePosition(row_index, column_index))

    def register_position(self, pos: SquarePosition) -> None:
        if pos in self.goal_states:
            self.goal_states.remove(pos)

    def is_done(self) -> bool:
        return not self.goal_states
