from advent_of_code_2021.day04.board import Board


class Game:
    def __init__(self, draw_numbers: list, board: Board):
        self.draw_numbers = draw_numbers
        self.board = board
