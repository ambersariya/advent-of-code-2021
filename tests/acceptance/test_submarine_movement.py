from submarine import Submarine


def test_should_return_interpreted_position_for_submarine(movement_commands):
    submarine = Submarine()
    actual_pos = submarine.move(commands=input)
    assert actual_pos == 150
