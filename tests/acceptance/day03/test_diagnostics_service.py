import pytest

from advent_of_code_2021.day03.diagnostics_service import DiagnosticsService


@pytest.fixture
def raw_report():
    return ["00100",
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


def test_return_diagnostics_report_from_raw_readings(raw_report):
    diagnostics_service = DiagnosticsService()
    report = diagnostics_service.generate_report(raw_report=raw_report)

    assert report.power_consumption == 198
    assert report.gamma_rate == 22
    assert report.epsilon_rate == 9
    assert report.oxygen_generator_rate == 23
    assert report.co2_scrubber_rate == 10
    assert report.life_support_rate == 230
