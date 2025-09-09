import pytest

from l_0074_search_a_2d_matrix.solution import Solution


@pytest.mark.parametrize(
    "matrix,target,expected_result",
    (
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
        ([[1]], 1, True),
        ([[1, 3, 5, 7]], 3, True),
        ([[1, 3]], 3, True),
    ),
)
def test(matrix: list[list[int]], target: int, expected_result: bool):

    assert Solution().searchMatrix(matrix, target) is expected_result
