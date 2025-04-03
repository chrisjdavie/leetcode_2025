import pytest

from l_0080_remove_duplicated_from_sorted_array_ii.solution import Solution


@pytest.mark.parametrize(
    "nums,expected_element_count,expected_nums",
    (
        ([1,1,1,2,2,3],5,[1,1,2,2,3]), # leetcode example 1
        ([0,0,1,1,1,1,2,3,3],7,[0,0,1,1,2,3,3]), # leetcode example 2
        ([1],1,[1]),
    )
)
def test(nums, expected_element_count, expected_nums):

    actual_element_count: int = Solution().removeDuplicates(nums)

    assert actual_element_count == expected_element_count
    assert expected_nums == nums[:len(expected_nums)]
