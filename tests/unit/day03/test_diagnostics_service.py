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


def test_should_return_diagnostic_report_from_multiple_raw_readings():
    raw_report = ['00100', '10101']
    diagnostics_service = DiagnosticsService()
    report = diagnostics_service.generate_report(raw_report=raw_report)

    assert report.gamma_rate == 21
    assert report.epsilon_rate == 10
    assert report.power_consumption == 210
