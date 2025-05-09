import pytest

from l_0200_number_of_islands.solution import Solution

@pytest.mark.parametrize(
    "grid,expected_output",
    (
        (
            [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ],
            1
        ),
        (
            [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ],
            3
        )
    )
)
def test(grid, expected_output):
    assert Solution().numIslands(grid) == expected_output
