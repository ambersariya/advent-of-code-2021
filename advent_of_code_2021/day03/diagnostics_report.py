from dataclasses import dataclass


@dataclass(frozen=True, init=True)
class DiagnosticsReport:
    gamma_rate: int
    epsilon_rate: int
    oxygen_generator_rate: int
    co2_scrubber_rate: int

    @property
    def power_consumption(self):
        return self.epsilon_rate * self.gamma_rate

    @property
    def life_support_rate(self):
        return self.oxygen_generator_rate * self.co2_scrubber_rate
