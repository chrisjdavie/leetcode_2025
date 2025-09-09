import pytest

from l_0283_move_zeroes.solution import Solution


@pytest.mark.parametrize(
    "nums,expected_output",
    [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([4, 7, 9, 2], [4, 7, 9, 2]),
    ],
)
def test(nums, expected_output):
    Solution().moveZeroes(nums)
    assert nums == expected_output
