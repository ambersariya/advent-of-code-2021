import importlib
import sys

if __name__ == '__main__':
    day = sys.argv[1]
    run = importlib.import_module(f'advent_of_code_2021.{day}.run')
    run.run()
