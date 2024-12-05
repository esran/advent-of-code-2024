import math

print("..loading day05")


def get_page_ordering(data: list[str]) -> list[tuple[int, int]]:
    result = []

    for i, line in enumerate(data):
        if len(line) == 0:
            break

        a,b = (int(x) for x in line.split("|"))
        result.append((a,b))

    return result


def get_updates(data: list[str]) -> list[list[int]]:
    result = []

    in_updates = False
    for line in data:
        if len(line) == 0:
            in_updates = True
            continue

        if not in_updates:
            continue

        result.append([int(x) for x in line.split(",")])

    return result

def check_update_ordered(update: list[int], ordering: list[tuple[int, int]]) -> bool:
    for index in range(len(update)):
        for other in range(index+1, len(update)):
            for order in ordering:
                if order[0] == update[other] and order[1] == update[index]:
                    return False

    return True

def get_middle_page(update: list[int]) -> int:
    half = int(len(update)/2)
    return update[half]

def fix_ordering(update: list[int], ordering:list[tuple[int, int]]) -> list[int]:
    while not check_update_ordered(update, ordering):
        update = do_ordering(update, ordering)

    return update

def do_ordering(update: list[int], ordering:list[tuple[int, int]]) -> list[int]:
    for i in range(len(update)-1):
        for order in ordering:
            if update[i] == order[1] and update[i+1] == order[0]:
                x = update[i]
                update[i] = update[i+1]
                update[i+1] = x

    return update

def func1(data: list[str]):
    result = 0

    ordering = get_page_ordering(data)
    updates = get_updates(data)

    for update in updates:
        if check_update_ordered(update, ordering):
            result += get_middle_page(update)

    return result

def func2(data: list[str]):
    result = 0

    ordering = get_page_ordering(data)
    updates = get_updates(data)

    for update in updates:
        if not check_update_ordered(update, ordering):
            new_update = fix_ordering(update, ordering)
            result += get_middle_page(new_update)

    return result
