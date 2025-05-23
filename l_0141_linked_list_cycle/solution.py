from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head.next

        while True:
            if fast is None or fast.next is None:
                return False
            if fast is slow:
                return True
            slow = slow.next
            fast = fast.next.next
