import re

print("..loading day04")


def find_adjacent_letter(data: list[str], start_line: int, start_pos: int, letter: str):
    if start_line > 0:
        if start_pos > 0:
            if data[start_line - 1][start_pos - 1] == letter:
                yield start_line - 1, start_pos - 1
        if data[start_line - 1][start_pos] == letter:
            yield start_line - 1, start_pos
        if start_pos + 1 < len(data[0]):
            if data[start_line - 1][start_pos + 1] == letter:
                yield start_line - 1, start_pos + 1

    if start_pos > 0:
        if data[start_line][start_pos - 1] == letter:
            yield start_line, start_pos - 1
    if start_pos + 1 < len(data[0]):
        if data[start_line][start_pos + 1] == letter:
            yield start_line, start_pos + 1

    if start_line + 1 < len(data):
        if start_pos > 0:
            if data[start_line + 1][start_pos - 1] == letter:
                yield start_line + 1, start_pos - 1
        if data[start_line + 1][start_pos] == letter:
            yield start_line + 1, start_pos
        if start_pos + 1 < len(data[0]):
            if data[start_line + 1][start_pos + 1] == letter:
                yield start_line + 1, start_pos + 1


def check_direction_match(
    data: list[str],
    start_line: int,
    start_pos: int,
    direction: tuple[int, int],
    search_word: str,
    letter: int,
) -> bool:
    # print(f"{search_word[letter]}: {start_line},{start_pos} = {data[start_line][start_pos]} -> {direction}")
    # If we don't match the current letter then no match
    if data[start_line][start_pos] != search_word[letter]:
        # print("mis-match")
        return False

    # If we're at the end of the word then we've matched!
    if letter + 1 >= len(search_word):
        # print("match")
        return True

    # If we can't move in the specified direction then no match
    next_line = start_line + direction[0]
    next_pos = start_pos + direction[1]
    if next_line < 0 or next_line >= len(data) or next_pos < 0 or next_pos >= len(data[0]):
        # print("edge out")
        return False

    # recurse to the next position
    return check_direction_match(
        data,
        next_line,
        next_pos,
        direction,
        search_word,
        letter + 1,
    )


def func1(data: list[str]):
    result = 0

    directions: list[tuple[int, int]] = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    for i in range(len(data)):
        for j in range(len(data[0])):
            for direction in directions:
                if check_direction_match(data, i, j, direction, "XMAS", 0):
                    result += 1

    return result

def get_direction_letter(data: list[str], i: int, j: int, direction: tuple[int, int]) -> str:
    return data[i+direction[0]][j+direction[1]]

def func2(data: list[str]):
    result = 0

    for i in range(1, len(data)-1):
        for j in range(1, len(data[0])-1):
            if data[i][j] == 'A':
                a_letters = []
                a_letters.append(get_direction_letter(data, i, j, (-1,-1)))
                a_letters.append(get_direction_letter(data, i, j, (1,1)))
                b_letters = []
                b_letters.append(get_direction_letter(data, i, j, (1,-1)))
                b_letters.append(get_direction_letter(data, i, j, (-1,1)))
                if set("MS") == set(a_letters) and set("MS") == set(b_letters):
                    result += 1

    return result
