#!/usr/bin/env python3
from turbozzle.creator.levels import FILE_TO_LEVEL_MAP, get_color


def test_get_color_1() -> None:
    assert get_color("r") == "red"


def test_level_length_1() -> None:
    for level in FILE_TO_LEVEL_MAP.values():
        assert len(level) == 13
        for row in level:
            assert len(row) == 13
