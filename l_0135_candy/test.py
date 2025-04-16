import pytest

from l_0135_candy.solution import Solution

@pytest.mark.parametrize(
    "ratings,expected_output",
    (
        ([6, 5, 8, 7, 6, 5, 6], 15),
        ([1,0,2], 5),
        ([1,2,2], 4),
        ([4], 1),
        ([2, 1], 3),
        ([1, 2], 3),
    )
)
def test(ratings, expected_output):

    assert Solution().candy(ratings) == expected_output
