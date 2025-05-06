from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited: set[ListNode] = set()

        prev_node: Optional[ListNode] = head

        while True:
            if prev_node is None:
                return False
            if prev_node in visited:
                return True
            
            visited.add(prev_node)
            prev_node = prev_node.next
