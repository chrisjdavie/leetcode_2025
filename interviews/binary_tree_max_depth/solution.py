from __future__ import annotations
from typing import Optional

from dataclasses import dataclass


@dataclass
class Node:

    left: Optional[Node] = None
    right: Optional[Node] = None


def max_depth(this_node: Optional[Node]) -> int:
    if this_node is None:
        return 0

    return 1 + max(
        (
            max_depth(this_node.left),
            max_depth(this_node.right)
        )
    )
