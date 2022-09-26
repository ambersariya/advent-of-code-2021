import pytest

from advent_of_code_2021.depth_calculator import calculate_depth, NotEnoughReadings


def test_raises_exceptions_when_there_is_less_than_2_measurements():
    sonar_readings = [100]
    with pytest.raises(NotEnoughReadings):
        calculate_depth(readings=sonar_readings)


@pytest.mark.parametrize('sonar_readings, expected_increase', [
    ([100, 101, 102, 103, 105], 4),
    ([100, 101, 102], 2),
    ([100, 101], 1),
    ([100, 100], 0),
])
def test_returns_calculated_depth_increase(sonar_readings, expected_increase):
    result = calculate_depth(readings=sonar_readings)
    assert result == expected_increase
