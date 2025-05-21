import pytest

from l_0909_snakes_and_ladders.solution import Solution, pos_to_coords


# @pytest.mark.parametrize(
#     "board,expected_result",
#     (
#         (
#             [
#                 [-1,-1,-1,-1,-1,-1],
#                 [-1,-1,-1,-1,-1,-1],
#                 [-1,-1,-1,-1,-1,-1],
#                 [-1,35,-1,-1,13,-1],
#                 [-1,-1,-1,-1,-1,-1],
#                 [-1,15,-1,-1,-1,-1]
#             ],
#             4,
#         ),
#         (
#             [
#                 [-1,-1],
#                 [-1,3]
#             ],
#             1,
#         ),
#         # not working case -> -1
#     )
# )
# def test(board, expected_result):
#     assert Solution().snakesAndLadders(board) == expected_result

@pytest.mark.parametrize(
    "pos,width,expected_coords",
    (
        (1,6,(5,0)),
        (6,6,(5,5)),
        (7,6,(4,5)),
    )
)
def test(pos, width, expected_coords):
    assert pos_to_coords(pos, width) == expected_coords
