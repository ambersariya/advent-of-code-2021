class NotEnoughReadings(Exception):
    pass


class NotEnoughReadingsToConvert(Exception):
    pass


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


def convert_readings(sonar_readings):
    if len(sonar_readings) < 3:
        raise NotEnoughReadingsToConvert()
