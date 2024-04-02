from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    m = set()
    while headA:
        m.add(headA)
        headA = headA.next
    
    while headB:
        if headB in m:
            return headB
        headB = headB.next
        
    return None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    a = headA
    b = headB

    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a

def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:

    a = headA
    b = headB

    l1, l2 = 1, 1

    while a or b:
        if a:
            l1 += 1
            a = a.next
        if b:
            l2 += 1
            b = b.next

    if l2 - l1 > 0:
        for i in range(l2-l1):
            headB = headB.next
        
    else:
        for i in range(l1-l2):
            headA = headA.next


    while headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    
    return None