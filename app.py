import sys

from advent_of_code_2021.submarine import Submarine


def readings(input: str):
    with open(input) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]


puzzle_input_filepath = sys.argv[1]
puzzle_input = readings(input=puzzle_input_filepath)
# sliding_window_readings = convert_readings(sonar_readings=sonar_readings(input=puzzle_input))
# result = calculate_depth(readings=sliding_window_readings)

submarine = Submarine()

result = submarine.move(commands=puzzle_input)

print(result)
