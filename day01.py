import shlex


print("..loading day01")

def func1(data: list[str]):
    first = []
    second = []
    for line in data:
        values = shlex.split(line)
        first.append(values[0])
        second.append(values[1])

    first.sort()
    second.sort()

    result = 0
    for v1, v2 in zip(first, second):
        diff = abs(int(v2) - int(v1))
        result += diff

    return result


def func2(data: list[str]):
    first = []
    second = []
    for line in data:
        values = shlex.split(line)
        first.append(values[0])
        second.append(values[1])

    result = 0
    for n in first:
        occurences = len([x for x in second if x == n])
        score = int(n) * occurences
        result += score

    return result
