import importlib
import sys


def run_puzzle(day):
    run = importlib.import_module(f'advent_of_code_2021.{day}.run')
    run.run()


if __name__ == '__main__':
    day = sys.argv[1]
    run_puzzle(day)
