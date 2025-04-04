import pytest

from l_0169_majority_element.solution import Solution


@pytest.mark.parametrize(
    "nums,expected_majority_element",
    (
        ([3,2,3], 3),
        ([2,2,1,1,1,2,2], 2),
    )
)
def test(nums, expected_majority_element):

    actual_majority_element: int = Solution().majorityElement(nums)
    assert actual_majority_element == expected_majority_element
