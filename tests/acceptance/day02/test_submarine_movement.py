from advent_of_code_2021.day02.submarine import Submarine


def test_should_return_interpreted_position_for_submarine(movement_commands):
    submarine = Submarine()
    actual_pos = submarine.move(commands=movement_commands)
    assert actual_pos == 900
