from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    
    a = ListNode(val=head.val, next=None)
    head = head.next

    while head:
        tmp = ListNode(val=head.val, next=a)
        a = tmp
        head = head.next
    return a