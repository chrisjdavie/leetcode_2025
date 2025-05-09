from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    _large_number: int = 10**5 + 1

    def _getMax(self, node: TreeNode) -> int:
        if node.right is not None:
            return self._getMax(node.right)
        return node.val

    def _getMin(self, node: TreeNode) -> int:
        if node.left is not None:
            return self._getMin(node.left)
        return node.val

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return self._large_number

        cands: list[int] = []

        if root.left is not None:
            max_left: int = self._getMax(root.left)
            cands.append(root.val - max_left)
            cands.append(self.getMinimumDifference(root.left))

        if root.right is not None:
            min_right: int = self._getMin(root.right)
            cands.append(min_right - root.val)
            cands.append(self.getMinimumDifference(root.right))

        return min(cands)
