from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class BoardResponse:
    victory: bool
    rounds_passed: int
    is_last_number_present: bool
