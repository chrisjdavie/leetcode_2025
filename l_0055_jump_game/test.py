import pytest

from l_0055_jump_game.solution import Solution


@pytest.mark.parametrize(
    "nums,expected_output",
    (
        ([2,3,1,1,4], True), # succeeds
        ([3,2,1,0,4], False), # gets stuck at zero
        ([8,1], True),
        ([0], True),
        ([1], True),
        ([1,2], True),
        ([2,0], True)
    )
)
def test(nums, expected_output):

    actual_output: bool = Solution().canJump(nums)

    assert actual_output == expected_output
