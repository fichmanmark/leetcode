from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    return max(maxDepth(root.left), maxDepth(root.right)) + 1


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    queue = [root]
    max_depth = 0
    while queue:
        max_depth += 1
        for i in range(len(queue)):
            curr = queue.pop(0)
            if curr.left:
                queue += [curr.left]
            if curr.right:
                queue += [curr.right]
    return max_depth

