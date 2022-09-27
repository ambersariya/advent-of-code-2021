from advent_of_code_2021.day01.sonar import convert_readings, calculate_depth

PUZZLE_INPUT = 'puzzles/day01.txt'


def read_file(filepath: str) -> list:
    with open(filepath) as file:
        lines = file.readlines()
        return [int(line.rstrip()) for line in lines]


def run():
    sonar_readings = read_file(filepath=PUZZLE_INPUT)
    sliding_window_readings = convert_readings(sonar_readings=sonar_readings)
    result = calculate_depth(readings=sliding_window_readings)
    print(result)
