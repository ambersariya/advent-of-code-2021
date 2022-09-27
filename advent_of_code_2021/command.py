from dataclasses import dataclass


@dataclass(frozen=True, init=True)
class Command:
    direction: str
    input_value: int
