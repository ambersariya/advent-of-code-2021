import pytest

from advent_of_code_2021.day03.diagnostics_service import DiagnosticsService


@pytest.fixture
def raw_report():
    return ["0b00100",
            "0b11110",
            "0b10110",
            "0b10111",
            "0b10101",
            "0b01111",
            "0b00111",
            "0b11100",
            "0b10000",
            "0b11001",
            "0b00010",
            "0b01010"]


def test_diagnostics_report_checks_power_consumption(raw_report):
    diagnostics_service = DiagnosticsService()
    report = diagnostics_service.generate_report(raw_report=raw_report)

    assert report.power_consumption == 198
    assert report.gamma_rate == 22
    assert report.epsilon_rate == 9
