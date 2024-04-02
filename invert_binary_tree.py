from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    new_tree = root
    new_tree.left, new_tree.right = invertTree(new_tree.right), invertTree(new_tree.left)

    return new_tree
