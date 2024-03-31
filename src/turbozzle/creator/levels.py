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

LEVEL_0 = [
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "g", "b", "b", "b", "b", "b", "b", "b", "b", "b", "y", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
]


LEVEL_1 = [
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


LEVEL_6 = [
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "b", "b", "b", "b", "b", "b", "b", "b", "b", "x"],
    ["x", "x", "x", "b", "x", "x", "x", "x", "x", "x", "x", "b", "x"],
    ["x", "x", "x", "b", "x", "b", "b", "b", "b", "b", "x", "b", "x"],
    ["x", "x", "x", "b", "x", "b", "x", "x", "x", "b", "x", "b", "x"],
    ["x", "x", "x", "b", "x", "b", "x", "y", "x", "b", "x", "b", "x"],
    ["x", "x", "x", "b", "x", "b", "b", "b", "x", "b", "x", "b", "x"],
    ["x", "x", "x", "b", "x", "x", "x", "x", "x", "b", "x", "b", "x"],
    ["x", "x", "x", "b", "b", "b", "b", "b", "b", "b", "x", "b", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "b", "x"],
    ["x", "g", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
]

# A tree of some sort with yellow on the "leaves"
LEVEL_7 = [
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

COLOR_MAPPING = {
    "g": "green",
    "x": "black",
    "b": "blue",
    "y": "yellow",
    "r": "red",
}


def get_color(color_code: str) -> str:
    return COLOR_MAPPING[color_code]


FILE_TO_LEVEL_MAP = {
    "puzzle_0.png": LEVEL_0,
    "puzzle_1.png": LEVEL_1,
    "puzzle_2.png": LEVEL_2,
    "puzzle_3.png": LEVEL_3,
    "puzzle_6.png": LEVEL_6,
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
