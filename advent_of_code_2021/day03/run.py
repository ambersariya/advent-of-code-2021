import string

from advent_of_code_2021.day03.diagnostics_service import DiagnosticsService

PUZZLE_INPUT = 'puzzles/day03.txt'


def read_file(filepath: str):
    with open(filepath) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]


def run():
    puzzle_input = read_file(filepath=PUZZLE_INPUT)
    service = DiagnosticsService()
    report = service.generate_report(raw_report=puzzle_input)
    template = string.Template("""
    power_consumption=$power_consumption
    life_support_rate=$life_support_rate
    """)
    print(template.safe_substitute(
        power_consumption=report.power_consumption,
        life_support_rate=report.life_support_rate
    ))
