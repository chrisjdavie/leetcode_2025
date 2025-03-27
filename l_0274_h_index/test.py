import pytest

from l_0274_h_index.solution import Solution


@pytest.mark.parametrize(
    "citations,expected_h_index",
    (
        ([3,0,6,1,5], 3),
        ([1,3,1], 1),
        ([5,5,5,5], 4),
        ([3,3,3], 3),
        ([3,3,2], 2),
    )
)
def test(citations, expected_h_index):

    actual_h_index: int = Solution().hIndex(citations)

    assert actual_h_index == expected_h_index
