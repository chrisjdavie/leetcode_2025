def find_maxima(height: list[int]) -> list[int]:
    if not height:
        return []
    if len(height) == 1:
        if height[0] > 0:
            return [0]
        return []

    maximas: list[int] = []

    if height[0] > height[1]:
        maximas.append(0)

    for i, (h_i, h_i_p_1, h_i_p_2) in enumerate(zip(height, height[1:], height[2:])):
        if h_i < h_i_p_1 and h_i_p_1 > h_i_p_2:
            maximas.append(i + 1)

    if height[-2] < height[-1]:
        maximas.append(len(height) - 1)

    return maximas
