from submarine import Submarine


def test_interpreted_position_is_at_zero():
    submarine = Submarine()
    actual_position = submarine.move(commands=[])
    assert actual_position == 0
