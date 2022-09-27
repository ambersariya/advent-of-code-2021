class Position:

    def __init__(self, distance: int = 0, depth: int = 0):
        self.depth = depth
        self.distance = distance

    def update_distance(self, input_value: int):
        self.distance += input_value

    def decrease_depth(self, input_value: int):
        self.depth -= input_value

    def increase_depth(self, input_value: int):
        self.depth += input_value

    def calculate_position(self) -> int:
        return self.depth * self.distance
