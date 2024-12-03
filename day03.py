import re

print("..loading day03")

def func1(data: list[str]):
    result = 0
    for line in data:
        matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
        for mul in matches:
            a, b = mul
            result += int(a) * int(b)

    return result

def func2(data: list[str]):
    enabled = True
    result = 0

    for line in data:
        matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
        for op in matches:
            if op.startswith("don't"):
                enabled = False
            elif op.startswith("do"):
                enabled = True
            elif enabled:
                numbers = re.findall(r"\d+", op)
                result += int(numbers[0]) * int(numbers[1])

    return result



