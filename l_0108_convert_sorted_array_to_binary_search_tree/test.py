from collections import deque

import pytest

from l_0108_convert_sorted_array_to_binary_search_tree.solution import Solution, TreeNode

@pytest.mark.parametrize(
    "nums,expected_outputs",
    (
        (
            [-10,-3,0,5,9],
            (
                [0,-3,9,-10,None,5],
                [0,-10,5,None,-3,None,9],
            )
        ),
        (
            [1,3],
            (
                [1,None,3],
                [3,1],
            ),
        )
    )
)
def test(nums, expected_outputs):

    trunk: TreeNode | None = Solution().sortedArrayToBST(nums)

    queue: deque[TreeNode | None] = deque([trunk])
    linearised: list[int] = []

    while queue:
        next_node: TreeNode | None = queue.popleft()
        if next_node:
            linearised.append(next_node.val)
            queue.append(next_node.left)
            queue.append(next_node.right)
        else:
            linearised.append(None)
    
    while linearised and linearised[-1] is None:
        linearised.pop()

    assert linearised in expected_outputs


@pytest.mark.parametrize(
    "nums",
    (
        ([-10,-3,0,5,9,10,11,12,13,14],),
    )
)
def test_explore(nums):

    trunk: TreeNode | None = Solution().sortedArrayToBST(nums)

    min_height: int = 1000000000000000000000
    max_height: int = -1

    def _explore(node: TreeNode, depth: int):
        nonlocal min_height, max_height
        if node is None:
            min_height = min((min_height, depth))
            max_height = max((max_height, depth))
            return

        if node.left is not None:
            assert node.left.val < node.val
        if node.right is not None:
            assert node.right.val > node.val

        _explore(node.left, depth+1)
        _explore(node.right, depth+1)
    
    _explore(trunk, 0)

    assert min_height == max_height or min_height == max_height - 1