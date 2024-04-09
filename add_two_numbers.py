# MEDIUM
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mem = 0
        num = ListNode()
        num_head = num
        while l1 and l2:
            new_value = l1.val + l2.val + mem
            if new_value > 9:
                mem = 1
                new_value = new_value % 10
            else:
                mem = 0
            new_node = ListNode(val=new_value)
            num.next = new_node
            num = new_node
            l1 = l1.next
            l2 = l2.next
        
        l1 = l1 if l1 else l2
        while l1:
            new_value = l1.val + mem
            if new_value > 9:
                mem = 1
                new_value = new_value % 10
            else:
                mem = 0
            new_node = ListNode(val=new_value)
            num.next = new_node
            num = new_node
            l1 = l1.next
        if mem == 1:
            num.next = ListNode(val=1)
        return num_head.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        node = dummy
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            v = v1 + v2 + carry
            carry = v // 10
            v = v % 10
            node.next = ListNode(v)
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
