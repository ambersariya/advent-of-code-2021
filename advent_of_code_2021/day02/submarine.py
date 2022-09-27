from advent_of_code_2021.day02.command import Command
from advent_of_code_2021.day02.position import Position


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
