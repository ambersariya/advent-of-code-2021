class Board:
    def parse(self, raw_str: str) -> "Board":
        raise NotImplementedError()


def test_generate_a_board_from_string():
    raw_str = '''
22 13 17 11  0
8  2 23  4 24
21  9 14 16  7
6 10  3 18  5
1 12 20 15 19
'''
    board_parser = Board()
    game_board = board_parser.parse(raw_str=raw_str)

    assert game_board.rows == 5
    assert game_board.columns == 5
    assert game_board.number_at(column=1, row=0) == 13
    assert game_board.number_at(column=2, row=2) == 14

