from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while head:
            vals.append(head.val)
        
        return vals == vals[::-1]
    


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            prev = None
            while head:
                next_node = head.next
                head.next = prev
                prev = head
                head = next_node
            return prev

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        slow = reverse(slow)

        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
            
        return True
    

        

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        reversed_list = None
        fast, slow = head, head
        while fast and fast.next:
            tmp = slow
            fast = fast.next.next
            slow = slow.next
            tmp.next = reversed_list
            reversed_list = tmp

        
        if fast:
            slow = slow.next
            


        while reversed_list and reversed_list.val == slow.val:
            reversed_list = reversed_list.next
            slow = slow.next
            
        return reversed_list is None

    



assert Solution().isPalindrome([1,2,2,1]) == True
assert Solution().isPalindrome([1,2]) == False
