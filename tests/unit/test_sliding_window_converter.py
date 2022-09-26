import pytest

from advent_of_code_2021.depth_calculator import NotEnoughReadingsToConvert, convert_readings


def test_raise_error_when_less_than_three_readings_are_provided():
    sonar_readings = [1, 2]

    with pytest.raises(NotEnoughReadingsToConvert):
        convert_readings(sonar_readings)


def test_convert_sonar_readings_into_list_of_sliding_window_readings():
    sonar_readings = [1, 2, 3]
    sliding_window_readings = convert_readings(sonar_readings=sonar_readings)

    assert sliding_window_readings == [6]


def test_convert_list_of_4_sonar_readings_to_1_reading():
    sonar_readings = [1, 2, 3, 4]
    sliding_window_readings = convert_readings(sonar_readings=sonar_readings)

    assert sliding_window_readings == [6, 9]
