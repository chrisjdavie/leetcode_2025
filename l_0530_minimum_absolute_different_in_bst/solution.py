from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        prev: Optional[TreeNode] = None
        min_diff: int = 10**5 + 1

        def _dfs(node: TreeNode):
            nonlocal prev
            nonlocal min_diff

            if node is None:
                return
            
            _dfs(node.left)
            if prev is not None:
                min_diff = min((min_diff, node.val - prev.val))
            prev = node
            _dfs(node.right)

        _dfs(root)

        return min_diff
