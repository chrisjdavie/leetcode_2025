import pytest

from l_0209_minimum_size_subarray_sum.solution import Solution

@pytest.mark.parametrize(
    "target,nums,expected_output",
    (
        (7, [2,3,1,2,4,3], 2),
        (4, [1,4,4], 1),
        (11, [1,1,1,1,1,1,1,1], 0),
    )
)
def test(target, nums, expected_output):

    assert expected_output == Solution().minSubArrayLen(target, nums)
