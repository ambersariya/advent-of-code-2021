from __future__ import annotations
from dataclasses import dataclass, field

from advent_of_code_2021.day04.board_response import BoardResponse


@dataclass(init=True)
class Board:
    board: list[list[int]]
    rounds_passed: int = field(default=0)

    @staticmethod
    def parse(raw_str: str) -> Board:
        board = []
        raw_str = raw_str.strip("\n")
        generate_rows = raw_str.split("\n")
        for row in generate_rows:
            row = list(filter(lambda r: len(r) > 0, row.split(" ")))
            row = list(map(int, row))
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
            if number in row:
                found = True
                break
        self.rounds_passed += 1
        return BoardResponse(
            victory=False,
            rounds_passed=self.rounds_passed,
            is_last_number_present=found
        )
