import shlex

def split_line(line: str):
    total, numbers = line.split(":")
    numbers = [int(num) for num in shlex.split(numbers)]
    return int(total), numbers

def calc(numbers: list[int], check: int, include_concat: bool = False):
    if len(numbers) == 1:
        yield check + numbers[0]
        yield check * numbers[0]
        if include_concat:
            yield int(f"{check}{numbers[0]}")
    else:
        for sub in calc(numbers[1:], check + numbers[0], include_concat):
            yield sub
        for sub in calc(numbers[1:], check * numbers[0], include_concat):
            yield sub
        if include_concat:
            for sub in calc(numbers[1:], int(f"{check}{numbers[0]}"), include_concat):
                yield sub

def func1(data: list[str]):
    result = 0

    for _, line in enumerate(data):
        total, numbers = split_line(line)

        check = numbers[0]
        for sub in calc(numbers[1:], check):
            if sub == total:
                result += total
                break

    return result

def func2(data: list[str]):
    result = 0

    for _, line in enumerate(data):
        total, numbers = split_line(line)

        check = numbers[0]
        for sub in calc(numbers[1:], check, True):
            if sub == total:
                result += total
                break

    return result
