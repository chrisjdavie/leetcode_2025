from collections import deque

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        nodes: deque[tuple[TreeNode, int]] = deque([(root, 0)])

        right_side_view: list[int] = []

        while nodes:
            curr_node, depth = nodes.popleft()
            if curr_node is None:
                continue

            if len(right_side_view) == depth:
                right_side_view.append(-101)
            right_side_view[depth] = curr_node.val

            nodes.append((curr_node.left, depth+1))
            nodes.append((curr_node.right, depth+1))

        return right_side_view
