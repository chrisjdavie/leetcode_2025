from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow: ListNode = head
        fast: ListNode = head        

        while True:
            if fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
