from advent_of_code_2021.day03.diagnostics_report import DiagnosticsReport
from advent_of_code_2021.day03.error import NotEnoughRawData


class DiagnosticsService:
    def generate_report(self, raw_report: list[str]) -> DiagnosticsReport:
        if len(raw_report) == 0:
            raise NotEnoughRawData()
        binary_gamma = raw_report[0]
        binary_epsilon = ""
        for bit in binary_gamma:
            binary_epsilon += "1" if bit == "0" else "0"
        gamma_rate = int(binary_gamma, 2)
        epsilon_rate = int(binary_epsilon, 2)
        return DiagnosticsReport(gamma_rate=gamma_rate, epsilon_rate=epsilon_rate)
