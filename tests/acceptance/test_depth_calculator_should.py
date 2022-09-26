from advent_of_code_2021.depth_calculator import calculate_depth


def test_returns_number_of_times_depth_increases(sonar_readings):
    result = calculate_depth(readings=sonar_readings)
    assert result == 1709
