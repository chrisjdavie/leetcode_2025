import pytest

from l_0088_merge_sorted_array.solution import Solution


@pytest.mark.parametrize(
    "nums1,m,nums2,n,res",
    (
        ([1,2,3,0,0], 3, [4,5], 2, [1,2,3,4,5]),
        ([4,0], 1, [3], 1, [3,4]),
        ([2,4,0,0], 2, [1,3], 2, [1,2,3,4]),
        ([1,2,10,11,0,0,0,0], 4, [2,5,6,7], 4, [1,2,2,5,6,7,10,11]), # leetcode example 0
        ([1,2,10,11,0,0,0,0], 4, [2,5,12,13], 4, [1,2,2,5,10,11,12,13]), # leetcode example 0
        ([1,2,6,7,0,0], 4, [4,5], 2, [1,2,4,5,6,7]),
        ([4,5,6,7,8,9,10,0,0], 7, [2,3], 2, [2,3,4,5,6,7,8,9,10]),
        ([1,2,6,7,8,0,0], 5, [4,5], 2, [1,2,4,5,6,7,8]),
        ([1], 1, [], 0, [1]), # leetcode example 1
        ([0], 0, [1], 1, [1]), # leetcode example 2
        
    )
)
def test(nums1, m, nums2, n, res):

    Solution().merge(nums1, m, nums2, n)

    assert nums1 == res
