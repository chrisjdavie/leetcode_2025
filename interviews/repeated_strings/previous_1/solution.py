def reduce_repeated_strings(input_str: str, max_len: int) -> str:

    current_char: str = ""
    char_count: int = -1

    result: list[str] = []

    for this_char in input_str:
        if current_char != this_char:
            current_char = this_char
            char_count = 0
        if not (current_char == this_char and char_count >= max_len):
            result.append(current_char)
            char_count += 1

    return "".join(result)
