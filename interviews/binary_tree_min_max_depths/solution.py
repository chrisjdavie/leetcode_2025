from __future__ import annotations
from typing import Optional

from dataclasses import dataclass


@dataclass
class Node:

    left: Optional[Node] = None
    right: Optional[Node] = None


def min_max_depths(trunk_node: Optional[Node]) -> tuple[int, int]:

    min_depth: int = 10**9
    max_depth: int = -1

    def _find_depths(this_node: Optional[Node], depth) -> None:
        nonlocal min_depth, max_depth
        if this_node is None:
            min_depth = min((depth, min_depth))
            max_depth = max((depth, max_depth))
            return
        
        _find_depths(this_node.left, depth+1)
        _find_depths(this_node.right, depth+1)

    _find_depths(trunk_node, 0)

    return (min_depth, max_depth)
