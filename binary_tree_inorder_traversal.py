from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    nodes =  []
    if root.left:
        nodes.extend(inorderTraversal(root.left))
    
    nodes += [root.val]

    if root.right:
        return nodes.extend(inorderTraversal(root.right))
    
    return nodes