import shlex
from enum import Enum


class Direction(Enum):
    Increasing = 1
    Decreasing = -1
    Undefined = 0

def check_safe(numbers: list[int]) -> bool:
    direction = Direction.Undefined
    if numbers[0] < numbers[1]:
        direction = Direction.Increasing
    else:
        direction = Direction.Decreasing

    # Not safe if first two are equal
    if direction == Direction.Undefined:
        return False

    safe = True
    for i in range(1, len(numbers)):
        if direction == Direction.Increasing and numbers[i] <= numbers[i - 1]:
            safe = False
            break

        if direction == Direction.Decreasing and numbers[i] >= numbers[i - 1]:
            safe = False
            break

        if abs(numbers[i] - numbers[i - 1]) > 3:
            safe = False
            break

    return safe

def get_numbers_from_line(line: str):
    parts = shlex.split(line)
    return [int(p) for p in parts]



def func1(data: list[str]):
    safe_count = 0

    for line in data:
        numbers = get_numbers_from_line(line)

        if check_safe(numbers):
            safe_count += 1

    return safe_count

def func2(data: list[str]):
    safe_count = 0

    for line in data:
        numbers = get_numbers_from_line(line)

        if check_safe(numbers):
            safe_count += 1
            continue

        for i in range(len(numbers)):
            new_numbers = numbers.copy()
            del new_numbers[i]
            if check_safe(new_numbers):
                safe_count += 1
                break

    return safe_count
