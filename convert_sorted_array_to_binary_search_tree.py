from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(val=nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root

# less memory
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create_tree_rec(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(val=nums[mid])
            root.left = create_tree_rec(l, mid-1)
            root.right = create_tree_rec(mid+1, r)
            return root
        
        return create_tree_rec(0, len(nums)-1)