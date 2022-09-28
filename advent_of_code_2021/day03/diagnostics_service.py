from advent_of_code_2021.day03.diagnostics_report import DiagnosticsReport
from advent_of_code_2021.day03.error import NotEnoughRawData


def column(matrix, i):
    return [row[i] for row in matrix]


class DiagnosticsService:
    def generate_report(self, raw_report: list[str]) -> DiagnosticsReport:
        if len(raw_report) == 0:
            raise NotEnoughRawData()
        report_matrix = list(map(lambda entry: list(entry), raw_report))
        binary_gamma = ''
        for index in range(0, len(report_matrix[0])):
            columnar_bits = column(report_matrix, index)
            num_of_zeros = self.__num_of_zeros(columnar_bits)
            total_bits = len(columnar_bits)
            num_of_ones = total_bits - num_of_zeros
            binary_gamma += ('0' if num_of_zeros > num_of_ones else '1')
        binary_epsilon = self.__flip_bits(binary_gamma)

        return DiagnosticsReport(
            gamma_rate=int(binary_gamma, base=2),
            epsilon_rate=int(binary_epsilon, base=2)
        )

    @staticmethod
    def __flip_bits(bits: str):
        return bits.replace('1', 'x').replace('0', 'y').replace('x', '0').replace('y', '1')

    @staticmethod
    def __num_of_zeros(bits: list):
        return len(list(filter(lambda _bit: _bit == '0', bits)))
