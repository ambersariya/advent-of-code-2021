from day02.submarine import Submarine


def test_interpreted_position_is_at_zero():
    submarine = Submarine()
    actual_position = submarine.move(commands=[])
    assert actual_position == 0


def test_interpreted_position_is_at_minus_one_after_moving_one_and_increasing_depth_by_one():
    submarine = Submarine()
    actual_position = submarine.move(commands=["forward 1", "down 1"])
    assert actual_position == 1
