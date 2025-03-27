import pytest

from l_0045_jump_game_ii.solution import Solution


@pytest.mark.parametrize(
    "nums,expected_min_jumps",
    (
        ([2,3,1,1,4], 2),
        ([2,3,0,1,4], 2),
        ([1,1,1,1], 3),
        ([0], 0),
    )
)
def test(nums, expected_min_jumps):

    actual_min_jumps: int = Solution().jump(nums)

    assert actual_min_jumps == expected_min_jumps
