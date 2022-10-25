from advent_of_code_2021.day04.board import Board
from tests.unit.day04.conftest import RAW_STR

DRAW_NUMBERS = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]


def test_generate_a_board_from_string():
    game_board = Board.parse(raw_str=RAW_STR)

    assert game_board.rows == 5
    assert game_board.columns == 5
    assert game_board.number_at(column=1, row=0) == 21
    assert game_board.number_at(column=2, row=2) == 23


def test_check_if_a_number_is_present(game_board):
    response = game_board.check_number(number=7)

    assert response.victory is False
    assert response.rounds_passed == 1
    assert response.is_last_number_present is True


def test_check_if_a_number_is_not_present(game_board):
    response = game_board.check_number(number=99)

    assert response.victory is False
    assert response.rounds_passed == 1
    assert response.is_last_number_present is False


def test_check_if_we_can_roll_more_than_one_round(game_board):
    game_board.check_number(number=1)
    response = game_board.check_number(number=9)

    assert response.victory is False
    assert response.rounds_passed == 2
    assert response.is_last_number_present is True


def test_should_tell_us_about_victory_when_the_full_column_is_marked(game_board):
    game_board.check_number(number=14)
    game_board.check_number(number=10)
    game_board.check_number(number=18)
    game_board.check_number(number=22)
    response = game_board.check_number(number=2)

    assert response.victory is True
    assert response.rounds_passed == 5
    assert response.is_last_number_present is True
