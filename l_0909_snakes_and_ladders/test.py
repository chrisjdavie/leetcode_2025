import pytest

from l_0909_snakes_and_ladders.solution import Solution


@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "board,expected_result",
    (
        # single turn
        (
            [
                [-1, -1],
                [-1, -1]
            ],
            1
        ),
        # two turns
        (
            [
                [-1, -1, -1],
                [-1, -1, -1],
                [-1, -1, -1]
            ],
            2
        ),
        # shortcut with a ladder
        (
            [
                [-1, -1, -1, -1],
                [-1, -1, -1, -1],
                [-1, -1, -1, -1],
                [-1, 15, -1, -1],
            ],
            2
        ),
        # jump to end
        (
            [
                [-1, -1, -1],
                [-1, -1, -1],
                [-1,  9, -1]
            ],
            1
        ),
        # infinite loop (dfs)
        (
            [
                [-1,  1, -1],
                [-1, -1, -1],
                [-1,  7, -1]
            ],
            2
        ),
        # no solution, infinite loop (bfs)
        (
            [
                [ 1,  1, -1],
                [ 1,  1,  1],
                [-1,  1,  1]
            ],
            -1
        ),
        # chained snakes
        (
            [
                [-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1],
                [-1,-1,36,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1],
                [-1,15,-1,-1,-1,-1]
            ],
            3,
        ),
        # When linear exploration isn't furthest-first (leetcode test suite failure)
        (
            [
                [-1,7,-1],
                [-1,6,9],
                [-1,-1,2]
            ],
            1
        ),
        # leetcode test suite failure
        (
            [
                [-1,-1, 2,-1],
                [-1,-1,-1,-1],
                [-1,10,-1,-1],
                [-1,-1,-1, 8]
            ],
            2
        ),
        # leetcode test suite failure
        (
            [
                [-1,10,-1,15,-1],
                [-1,-1,18, 2,20],
                [-1,-1,12,-1,-1],
                [ 2, 4,11,18, 8],
                [-1,-1,-1,-1,-1]
            ],
            3
        ),
        # takes too long
        (
            [
                [-1,-1,30,14,15,-1],
                [23,9,-1,-1,-1,9],
                [12,5,7,24,-1,30],
                [10,-1,-1,-1,25,17],
                [32,-1,28,-1,-1,32],
                [-1,-1,23,-1,13,19]
            ],
            2
        ),
        # leetcodce test suite failure
        (
            [
                [-1,-1,27,13,-1,25,-1],
                [-1,-1,-1,-1,-1,-1,-1],
                [44,-1,8,-1,-1,2,-1],
                [-1,30,-1,-1,-1,-1,-1],
                [3,-1,20,-1,46,6,-1],
                [-1,-1,-1,-1,-1,-1,29],
                [-1,29,21,33,-1,-1,-1]
            ],
            4
        ),
    )
)
def test(board, expected_result):
    assert Solution().snakesAndLadders(board) == expected_result
