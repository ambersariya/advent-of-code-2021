from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class Board:
    board: list

    @staticmethod
    def parse(raw_str: str) -> "Board":
        board = []
        raw_str = raw_str.strip("\n")
        generate_rows = raw_str.split("\n")
        for row in generate_rows:
            row = list(filter(lambda r: len(r) > 0, row.split(" ")))
            board.append(row)
        return Board(board=board)

    @property
    def rows(self) -> int:
        return len(self.board)

    @property
    def columns(self) -> int:
        return len(self.board[0])

    def number_at(self, row: int, column: int) -> int:
        return int(self.board[row][column])


def test_generate_a_board_from_string():
    raw_str = '''
22 13 17 11  0
8  2 23  4 24
21  9 14 16  7
6 10  3 18  5
1 12 20 15 19
'''
    game_board = Board.parse(raw_str=raw_str)

    assert game_board.rows == 5
    assert game_board.columns == 5
    assert game_board.number_at(column=1, row=0) == 13
    assert game_board.number_at(column=2, row=2) == 14
