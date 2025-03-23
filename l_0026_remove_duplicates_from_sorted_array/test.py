import pytest

from l_0026_remove_duplicates_from_sorted_array.solution import Solution


@pytest.mark.parametrize(
    "nums,expected_count,expected_nums",
    (
        ([1,1,2],2,[1,2]),
        ([0,0,1,1,1,2,2,3,3,4],5,[0,1,2,3,4]),
    )
)
def test(nums, expected_count, expected_nums):

    actual_count: int = Solution().removeDuplicates(nums)

    assert actual_count == expected_count
    assert expected_nums == nums[:len(expected_nums)]
