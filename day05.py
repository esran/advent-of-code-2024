from bisect import bisect_left

print("..loading day05")


# see https://stackoverflow.com/a/2701189
def bi_contains(lst, item):
    """efficient `item in lst` for sorted lists"""
    # if item is larger than the last its not in the list, but the bisect would
    # find `len(lst)` as the index to insert, so check that first. Else, if the
    # item is in the list then it has to be at index bisect_left(lst, item)
    return (item <= lst[-1]) and (lst[bisect_left(lst, item)] == item)


def get_page_ordering(data: list[str]) -> list[tuple[int, int]]:
    result = []

    for _, line in enumerate(data):
        if len(line) == 0:
            break

        a, b = (int(x) for x in line.split("|"))
        result.append((a, b))

    # Sort the ordering for use with bi_contains for performance
    return sorted(result)


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
    for index in range(len(update) - 1):
        # If our ordering contains the reverse of what we
        # have then the update is not ordered
        if bi_contains(ordering, (update[index + 1], update[index])):
            return False

    return True


def get_middle_page(update: list[int]) -> int:
    half = int(len(update) / 2)
    return update[half]


def fix_ordering(update: list[int], ordering: list[tuple[int, int]]) -> list[int]:
    while not check_update_ordered(update, ordering):
        update = do_ordering(update, ordering)

    return update


def do_ordering(update: list[int], ordering: list[tuple[int, int]]) -> list[int]:
    for i in range(len(update) - 1):
        if bi_contains(ordering, (update[i + 1], update[i])):
            x = update[i]
            update[i] = update[i + 1]
            update[i + 1] = x

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
