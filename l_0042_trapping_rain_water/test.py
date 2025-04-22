import pytest

from l_0042_trapping_rain_water.solution import Solution


@pytest.mark.parametrize(
    "heights,expected_water",
    (
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
        ([1,0], 0),
        ([2,0,3], 2),
        ([5], 0),
        ([4,2,0,3,2,5], 9),
        ([4,2,0,3,2,5,0,2,1,6], 9 + 12),
        ([1,1,0,1,1], 1),
    )
)
def test(heights, expected_water):

    assert Solution().trap(heights) == expected_water
