import sys

from advent_of_code_2021.submarine import convert_readings, calculate_depth


def sonar_readings(input: str):
    with open(input) as file:
        lines = file.readlines()
        return [int(line.rstrip()) for line in lines]


puzzle_input = sys.argv[1]
sliding_window_readings = convert_readings(sonar_readings=sonar_readings(input=puzzle_input))
result = calculate_depth(readings=sliding_window_readings)
print(result)
