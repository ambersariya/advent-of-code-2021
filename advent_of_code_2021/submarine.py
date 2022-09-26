class NotEnoughReadings(Exception):
    pass


class NotEnoughReadingsToConvert(Exception):
    pass


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
    def move(self, commands) -> int:
        return 0
