import pytest

from l_0088_merge_sorted_array.solution import Solution


@pytest.mark.parametrize(
    "nums1,m,nums2,n,expected_output",
    (
        ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    )
)
def test(nums1, m, nums2, n, expected_output):

    Solution().merge(nums1, m, nums2, n)

    assert nums1 == expected_output
