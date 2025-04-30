import pytest

from l_0228_summary_ranges.solution import Solution

@pytest.mark.parametrize(
    "nums,expected_output",
    (
        ([0,1,2,4,5,7], ["0->2","4->5","7"]),
        ([0,2,3,4,6,8,9], ["0","2->4","6","8->9"]),
        ([], []),
    )
)
def test(nums, expected_output):

    assert expected_output == Solution().summaryRanges(nums)
