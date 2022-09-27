from advent_of_code_2021.command import Command
from advent_of_code_2021.error import NotEnoughReadings, NotEnoughReadingsToConvert
from advent_of_code_2021.position import Position

SLIDING_WINDOW_SIZE = 3


def calculate_depth(readings: list[int]) -> int:
    if len(readings) <= 1:
        raise NotEnoughReadings()
    increase_times = 0
    last_depth = readings[0]
    for reading in readings[1:]:
        if reading > last_depth:
            increase_times += 1
        last_depth = reading

    return increase_times


def convert_readings(sonar_readings) -> list[int]:
    if len(sonar_readings) < SLIDING_WINDOW_SIZE:
        raise NotEnoughReadingsToConvert()
    last_valid_sliding_window_index = len(sonar_readings) - SLIDING_WINDOW_SIZE
    readings = []
    for index, _ in enumerate(sonar_readings[:last_valid_sliding_window_index + 1]):
        readings.append(sonar_readings[index] + sonar_readings[index + 1] + sonar_readings[index + 2])
    return readings


class Submarine:

    def __init__(self):
        self._position = Position()

    def move(self, commands: list) -> int:
        commands = self._parse_commands(commands)
        for command in commands:
            self._execute(command)
        return self._position.calculate_position()

    def _parse_commands(self, commands: list) -> list[Command]:
        def _parse_command(command: str) -> Command:
            direction, input_value = command.split(" ")
            return Command(direction=direction, input_value=int(input_value))

        return list(map(_parse_command, commands))

    def _execute(self, command: Command):
        match command.direction:
            case "forward":
                self.position = self._position.update_distance(command.input_value)
            case "up":
                self.position = self._position.decrease_depth(command.input_value)
            case "down":
                self.position = self._position.increase_depth(command.input_value)
