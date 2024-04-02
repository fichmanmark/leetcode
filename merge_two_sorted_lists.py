from typing import Optional
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    start = curr = ListNode(None)

    if list1 is None and list2 is None:
        return None
    
    
    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = ListNode(list1.val)
            list1 = list1.next
        else:
            curr.next = ListNode(list2.val)
            list2 = list2.next
        curr = curr.next


    if list1 or list2:
        curr = list1 if list1 else list2

    return start.next


def fill_nodes(l1, l2):
    start1 = ListNode(None)
    start2 = ListNode(None)
    curr1 = start1
    curr2 = start2

    for i in l1:
        curr1.next = ListNode(i)
        curr1 = curr1.next

    for i in l2:
        curr2.next = ListNode(i)
        curr2 = curr2.next


    return start1.next, start2.next
    

list1 = [1,2,4] 
list2 = [1,3,4]

list1, list2 = fill_nodes(list1, list2)

def get_l(start):
    l = []
    while start:
        l.append(start.val)
        start = start.next
    return l



print(get_l(list1), get_l(list2))

assert mergeTwoLists(list1, list2) == [1,1,2,3,4,4]


list1 = [] 
list2 = []
assert mergeTwoLists(list1, list2) == []


list1 = [] 
list2 = [0]
assert mergeTwoLists(list1, list2) == [0]

list1 = [] 
list2 = [0, 0]
assert mergeTwoLists(list1, list2) == [0, 0]
