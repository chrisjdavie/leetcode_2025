from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None


def binary_tree_to_ordered_list(trunk: Optional[TreeNode]) -> list[int]:
    
    ordered_list: list[int] = []

    def _dfs(node: Optional[TreeNode]):
        if node is None:
            return
        _dfs(node.left)
        ordered_list.append(node.val)
        _dfs(node.right)

    _dfs(trunk)

    return ordered_list
