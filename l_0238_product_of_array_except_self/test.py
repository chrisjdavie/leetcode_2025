import pytest

from l_0238_product_of_array_except_self.solution import Solution

@pytest.mark.parametrize(
    "nums,expected_output",
    (
        ([1,2,3,4], [24,12,8,6]),
        ([-1,1,0,-3,3], [0,0,9,0,0]),
    )
)
def test(nums, expected_output):

    assert Solution().productExceptSelf(nums) == expected_output
