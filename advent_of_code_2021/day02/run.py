from advent_of_code_2021.day02.submarine import Submarine

PUZZLE_INPUT = 'puzzles/day02.txt'


def read_file(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]


def run():
    puzzle_input = read_file(filepath=PUZZLE_INPUT)
    submarine = Submarine()
    result = submarine.move(commands=puzzle_input)
    print(result)
