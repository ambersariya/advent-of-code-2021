from functools import reduce


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


def convert_readings(sonar_readings) -> list[int]:
    if len(sonar_readings) < 3:
        raise NotEnoughReadingsToConvert()
    if len(sonar_readings) == 3:
        return [reduce(lambda a, b: a + b, sonar_readings)]
    last_reading_block_starts = len(sonar_readings) - 3
    readings = []
    for index, _ in enumerate(sonar_readings[:last_reading_block_starts+1]):
        readings.append(sonar_readings[index] + sonar_readings[index+1] + sonar_readings[index+2])
    return readings
