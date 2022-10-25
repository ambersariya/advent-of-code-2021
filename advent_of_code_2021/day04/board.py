from __future__ import annotations
from dataclasses import dataclass

from advent_of_code_2021.day04.board_response import BoardResponse


@dataclass(init=True, frozen=True)
class Board:
    board: list

    @staticmethod
    def parse(raw_str: str) -> Board:
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

    def check_number(self, number: int) -> BoardResponse:
        found = False
        for row in self.board:
            if str(number) in row:
                found = True
                break

        return BoardResponse(
            victory=False,
            rounds_passed=1,
            is_last_number_present=found
        )
