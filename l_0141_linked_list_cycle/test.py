from typing import Optional

import pytest

from l_0141_linked_list_cycle.solution import ListNode, Solution

@pytest.mark.parametrize(
    "head,pos,expected_output",
    (
        ([3,2,0,-4], 1, True),
        ([1,2], 0, True),
        ([0], -1, False),
        ([0, 0], -1, False)
    )
)
def test_cycle(head, pos, expected_output):

    head_node: ListNode = ListNode(head[0])
    prev_node: ListNode = head_node
    end_node: Optional[ListNode] = None

    if pos == 0:
        end_node: ListNode = head_node

    for i, current_val in enumerate(head[1:]):
        this_node: ListNode = ListNode(current_val)
        prev_node.next = this_node
        prev_node = this_node
        if pos == i + 1:
            end_node: ListNode = this_node

    prev_node.next = end_node

    assert Solution().hasCycle(head_node) == expected_output


def test_empty():
    assert Solution().hasCycle(None) == False
