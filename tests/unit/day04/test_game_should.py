from advent_of_code_2021.day04.board import Board
from advent_of_code_2021.day04.game import Game



BOARD = '''
14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
2  0 12  3  7'''


def test_game():
    game = Game(draw_numbers=DRAW_NUMBERS, board=Board.parse(raw_str=BOARD))
    round_result = game.next_step()

    assert round_result.numbers_drawn == 5
    assert round_result.won == False
