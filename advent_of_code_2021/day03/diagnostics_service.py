from advent_of_code_2021.day03.diagnostics_report import DiagnosticsReport
from advent_of_code_2021.day03.error import NotEnoughRawData


class DiagnosticsService:
    def generate_report(self, raw_report: list[str]) -> DiagnosticsReport:
        if len(raw_report) == 0:
            raise NotEnoughRawData()
