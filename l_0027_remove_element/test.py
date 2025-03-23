import pytest

from l_0027_remove_element.solution import Solution


@pytest.mark.parametrize(
    "nums,val,expected_count,expected_nums",
    (
        ([1,2,3,4,5],6,5,[1,2,3,4,5]),
        ([3,2,2,3],3,2,[2,2]), # leetcode example 1
        ([0,1,2,2,3,0,4,2],2,5,[0,1,4,0,3]), # leetcode example 2
    )
)
def test(nums,val,expected_count,expected_nums):

    actual_count: int = Solution().removeElement(nums, val)

    assert expected_count == actual_count
    assert sorted(expected_nums) == sorted(nums[:len(expected_nums)])
