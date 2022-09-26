import pytest

PUZZLE_INPUT_FILE = 'input_1.txt'


@pytest.fixture
def sonar_readings():
    with open(PUZZLE_INPUT_FILE) as file:
        lines = file.readlines()
        return [int(line.rstrip()) for line in lines]
