#!/usr/bin/python3

import os
import argparse
import sys
import datetime


def load_file(path: str) -> list[str]:
    if not os.path.exists(path):
        raise RuntimeError(f"Path does not exists: {path}")

    print(f"loading: {path}")
    with open(path, "r") as f:
        return f.read().splitlines()


def import_module(module_name: str):
    if module_name not in sys.modules:
        module = __import__(module_name)
        sys.modules[module_name] = module
    else:
        module = sys.modules[module_name]

    return module


def main():
    # Argument parsing to select the day to run for
    parser = argparse.ArgumentParser(prog="aoc-2024", description="Advent of Code 2024")
    parser.add_argument("day")
    args = parser.parse_args()

    if not args.day:
        raise ValueError("Required argument 'day' missing")

    day = f"day{int(args.day):02d}"

    day_module = import_module(day)

    data = load_file(f"{day}.input")

    for func in ["func1", "func2"]:
        try:
            start = datetime.datetime.now()
            result = getattr(day_module, func)(data)
            end = datetime.datetime.now()
            duration = end - start
            print(f"{day} {func} = {result} [{duration}]")
        except AttributeError:
            pass


if __name__ == "__main__":
    main()
