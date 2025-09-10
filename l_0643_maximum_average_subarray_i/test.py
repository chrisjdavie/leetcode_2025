from l_0643_maximum_average_subarray_i.solution import Solution

import pytest


@pytest.mark.parametrize(
    "nums,k,expected_output",
    (
        ([1, 12, -5, -6, 50, 3], 4, 12.75),
        ([5], 1, 5.0),
    ),
)
def test(nums: list[int], k: int, expected_output: float):

    assert Solution().findMaxAverage(nums, k) == expected_output
