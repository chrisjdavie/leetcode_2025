

def reduce_repeated_strings(input_str: str, max_len: int):
    if max_len == 0:
        return ""

    current_char: str = ""
    char_count: int = 0

    output_str: list[str] = []
    
    for this_char in input_str:
        if this_char == current_char and char_count >= max_len:
            continue
        if this_char != current_char:
            current_char = this_char
            char_count = 0
        output_str.append(this_char)
        char_count += 1
    
    return "".join(output_str)
