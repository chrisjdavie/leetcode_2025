import pytest

from mine.find_maxima.solution import find_maxima


@pytest.mark.parametrize(
    "heights,expected_maximas",
    (
        ([0,1,0,2,1,0,1,3,2,1,2,1], [1,3,7,10]),
        # ([1,0], [0]),
        # ([1,0,1], [0,2]),
        # ([1], [0])
    )
)
def test(heights, expected_maximas):

    assert find_maxima(heights) == expected_maximas
