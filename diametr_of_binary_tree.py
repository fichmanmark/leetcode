# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_max_depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.get_max_depth(root.left), self.get_max_depth(root.right))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_max_depth = self.get_max_depth(root.left)
        right_max_depth = self.get_max_depth(root.right)

        return max(left_max_depth + right_max_depth, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
    

class Solution:
    def get_depth_and_diameter(self, root):
        if root is None:
            return 0, 0
        
        left_dep, left_dia = self.get_depth_and_diameter(root.left)
        right_dep, right_dia = self.get_depth_and_diameter(root.right)

        cur_depth = max(left_dep, right_dep) + 1

        cir_dia = max(left_dep + right_dep, left_dia, right_dia)
        return cur_depth, cir_dia

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, dia = self.get_depth_and_diameter(root)
        return dia
    

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root):
            if root is None:
                return 0
            right = dfs(root.right)
            left = dfs(root.left)
            nonlocal ans
            ans = max(ans, right+left)
            return 1 + max(right, left)
        
        dfs(root)

        return ans
    

         
