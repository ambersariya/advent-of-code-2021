from dataclasses import dataclass


@dataclass(frozen=True, init=True)
class DiagnosticsReport:
    gamma_rate: int
    epsilon_rate: int

    @property
    def power_consumption(self):
        return self.epsilon_rate * self.gamma_rate
