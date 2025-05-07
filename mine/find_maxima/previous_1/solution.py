def find_maxima(height: list[int]) -> list[int]:
    if len(height) == 1:
        return [0]

    incline: bool = True
    results: list[int] = []

    for i, (h, h_p_1) in enumerate(zip(height[:-1], height[1:])):
        if h < h_p_1:
            incline = True
        if h > h_p_1:
            if incline:
                results.append(i)
            incline = False
    else:
        if incline:
            results.append(i+1)

    return results
