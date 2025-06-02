from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def _build(i_start: int, i_end: int) -> TreeNode:
            if i_start > i_end:
                return None

            i_mid: int = (i_start + (i_end - i_start)//2)

            return TreeNode(
                nums[i_mid],
                _build(i_start, i_mid - 1),
                _build(i_mid + 1, i_end),
            )

        return _build(0, len(nums) - 1)
