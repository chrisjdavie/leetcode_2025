import pytest

from l_0150_rotate_array.solution import Solution


@pytest.mark.parametrize(
    "nums,k,expected_nums",
    (
        ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
        ([-1,-100,3,99], 2, [3,99,-1,-100]),
        ([4], 0, [4]),
        ([1,2,3,4,5,6,7], 10, [5,6,7,1,2,3,4]),
    )
)
def test(nums, k, expected_nums):

    Solution().rotate(nums, k)

    assert nums == expected_nums
