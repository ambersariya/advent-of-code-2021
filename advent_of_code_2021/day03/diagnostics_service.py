from advent_of_code_2021.day03.diagnostics_report import DiagnosticsReport
from advent_of_code_2021.day03.error import NotEnoughRawData


def column(matrix, i):
    return [row[i] for row in matrix]


class DiagnosticsService:
    def generate_report(self, raw_report: list[str]) -> DiagnosticsReport:
        binary_gamma = self.binary_gamma(raw_report)
        binary_epsilon = self.__flip_bits(binary_gamma)

        return DiagnosticsReport(
            gamma_rate=int(binary_gamma, base=2),
            epsilon_rate=int(binary_epsilon, base=2),
            oxygen_generator_rate=self.generate_oxygen_rating(raw_report=raw_report),
            co2_scrubber_rate=self.co2_scrubber_rating(raw_report=raw_report)
        )

    def binary_gamma(self, raw_report) -> str:
        if len(raw_report) == 0:
            raise NotEnoughRawData()
        report_matrix = list(map(lambda entry: list(entry), raw_report))
        bin_gamma = ''
        for index in range(0, len(report_matrix[0])):
            columnar_bits = column(report_matrix, index)
            total_bits = len(columnar_bits)
            num_of_zeros = self.__num_of_zeros(columnar_bits)
            num_of_ones = total_bits - num_of_zeros
            bin_gamma += ('0' if num_of_zeros > num_of_ones else '1')
        return bin_gamma

    @staticmethod
    def __flip_bits(bits: str):
        return bits.replace('1', 'x').replace('0', 'y').replace('x', '0').replace('y', '1')

    @staticmethod
    def __num_of_zeros(bits: list):
        return len(list(filter(lambda _bit: _bit == '0', bits)))

    def generate_oxygen_rating(self, raw_report: list[str]) -> int:
        if len(raw_report) == 1:
            return int(raw_report[0], 2)
        report_matrix = list(map(lambda entry: list(entry), raw_report))
        bit_column_index = 0
        while len(report_matrix) > 1:
            most_common = []
            column_values = column(report_matrix, bit_column_index)
            common_bit = self.most_common_bit(bits=column_values)
            for reading in report_matrix:
                if reading[bit_column_index] == common_bit:
                    most_common.append(reading)
            bit_column_index += 1
            report_matrix = most_common
        return int("".join(report_matrix[0]), 2)

    def co2_scrubber_rating(self, raw_report: list[str]) -> int:
        if len(raw_report) == 1:
            return int(raw_report[0], 2)
        report_matrix = list(map(lambda entry: list(entry), raw_report))
        bit_column_index = 0
        while len(report_matrix) > 1:
            most_common = []
            column_values = column(report_matrix, bit_column_index)
            common_bit = self.least_common_bit(bits=column_values)
            for reading in report_matrix:
                if reading[bit_column_index] == common_bit:
                    most_common.append(reading)
            bit_column_index += 1
            report_matrix = most_common
        return int("".join(report_matrix[0]), 2)

    @staticmethod
    def most_common_bit(bits: list):
        starts_with_one = list(filter(lambda binary: binary == '1', bits))
        num_of_ones = len(starts_with_one)
        num_of_zeros = len(bits) - num_of_ones
        return "1" if num_of_ones >= num_of_zeros else "0"

    @staticmethod
    def least_common_bit(bits: list):
        starts_with_one = list(filter(lambda binary: binary == '1', bits))
        num_of_ones = len(starts_with_one)
        num_of_zeros = len(bits) - num_of_ones
        return "0" if num_of_zeros <= num_of_ones else "1"
