from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    fast, slow = head, head

    while fast:
        fast = fast.next
        fast = fast.next if fast else None
        slow = slow.next
        if fast == slow and fast:
            return True
    return False