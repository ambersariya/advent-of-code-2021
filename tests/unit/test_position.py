from advent_of_code_2021.day02.position import Position


def test_position_is_initially_zero():
    position = Position()
    assert position.aim == 0
    assert position.depth == 0
    assert position.horizontal == 0


def test_down_5_increases_aim_by_5_units():
    value = 5

    position = Position()
    position.increase_aim(down=value)

    assert position.aim == 5


def test_up_3_decreases_your_aim_by_3_units():
    value = 3

    position = Position()
    position.decrease_aim(up=value)

    assert position.aim == -3


def test_forward_increases_horizontal_position_and_depth():
    value = 3
    position = Position()
    position.increase_aim(down=value)
    position.update_distance(forward=value)

    assert position.horizontal == 3
    assert position.aim == 3
    assert position.depth == 9
