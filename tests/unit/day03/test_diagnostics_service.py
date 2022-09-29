import pytest

from advent_of_code_2021.day03.diagnostics_report import DiagnosticsReport
from advent_of_code_2021.day03.diagnostics_service import DiagnosticsService
from advent_of_code_2021.day03.error import NotEnoughRawData


def test_throw_error_when_not_enough_data_passed_in():
    raw_report = []
    diagnostics_service = DiagnosticsService()

    with pytest.raises(NotEnoughRawData):
        diagnostics_service.generate_report(raw_report=raw_report)


def test_should_return_diagnostic_report_with_one_raw_reading():
    raw_report = ['00100']
    diagnostics_service = DiagnosticsService()
    report = diagnostics_service.generate_report(raw_report=raw_report)

    assert isinstance(report, DiagnosticsReport)
    assert report.gamma_rate == 4
    assert report.epsilon_rate == 27
    assert report.power_consumption == 108
    assert report.oxygen_generator_rate == 4
    assert report.co2_scrubber_rate == 4
    assert report.life_support_rate == 16


def test_should_return_diagnostic_report_from_multiple_raw_readings():
    raw_report = ['00100', '10101']
    diagnostics_service = DiagnosticsService()
    report = diagnostics_service.generate_report(raw_report=raw_report)

    assert report.gamma_rate == 21
    assert report.epsilon_rate == 10
    assert report.power_consumption == 210
    assert report.oxygen_generator_rate == 21
    assert report.co2_scrubber_rate == 4
    assert report.life_support_rate == 84


def test_oxygen_generator_rating():
    raw_report = ["00100",
                  "11110",
                  "10110",
                  "10111",
                  "10101",
                  "01111",
                  "00111",
                  "11100",
                  "10000",
                  "11001",
                  "00010",
                  "01010"]
    diagnostics_service = DiagnosticsService()
    report = diagnostics_service.generate_oxygen_rating(raw_report=raw_report)
    assert report == 23


def test_co2_scrubber_rating():
    raw_report = ["00100",
                  "11110",
                  "10110",
                  "10111",
                  "10101",
                  "01111",
                  "00111",
                  "11100",
                  "10000",
                  "11001",
                  "00010",
                  "01010"]
    diagnostics_service = DiagnosticsService()
    report = diagnostics_service.co2_scrubber_rating(raw_report=raw_report)
    assert report == 10
