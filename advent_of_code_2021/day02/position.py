class Position:
    def __init__(self, horizontal: int = 0, depth: int = 0, aim: int = 0):
        self.aim = aim
        self.depth = depth
        self.horizontal = horizontal

    def update_distance(self, forward: int) -> "Position":
        self.horizontal += forward
        self.depth += (self.aim * forward)
        return self

    def increase_aim(self, down: int) -> "Position":
        self.aim += down
        return self

    def decrease_aim(self, up: int) -> "Position":
        self.aim -= up
        return self

    def calculate_position(self) -> int:
        return self.depth * self.horizontal
