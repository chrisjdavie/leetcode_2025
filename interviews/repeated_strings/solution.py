def reduce_repeated_strings(input_str: str, max_len: int) -> str:

    reduced: list[str] = []

    current_char: str = ""
    count: int = -1

    for this_char in input_str:
        if this_char != current_char:
            current_char = this_char
            count = 0
        if count < max_len:
            reduced.append(this_char)
            count += 1
    
    return "".join(reduced)
