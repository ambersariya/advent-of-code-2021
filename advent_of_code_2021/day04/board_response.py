from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class BoardResponse:
    victory: bool
    rounds_passed: int
    last_number_on_board: bool
