import pytest

from advent_of_code_2021.day04.board import Board

RAW_STR = '''
14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
2  0 12  3  7
'''


@pytest.fixture
def game_board():
    return Board.parse(raw_str=RAW_STR)
