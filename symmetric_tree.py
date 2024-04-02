from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def left_tranversal(root):
    res = []
    if not root:
        return [None]
    res += root.val
    if root.left:
        res += root.left.val
    if root.right:
        res += root.right.val
    res += left_tranversal(root.left)
    res += left_tranversal(root.right)
    return res

def right_tranversal(root):
    res = []
    res += root.val
    if root.right:
        res += root.right.val
    if root.left:
        res += root.left.val
    res += right_tranversal(root.right)
    res += right_tranversal(root.left)
    return res


def isSymmetric(root: Optional[TreeNode]) -> bool:
    rights = right_tranversal(root.right)
    lefts = left_tranversal(root.left)
    return rights == lefts


def isSymmetric(root: Optional[TreeNode]) -> bool:
    lefts, rights = [], []

    stack = [root.left]
    while stack:
        curr = stack.pop()
        if curr is None:
            lefts += [None]
            continue
        lefts += [curr.val]
        stack += [curr.left, curr.right]
        

    stack = [root.right]
    while stack:
        curr = stack.pop()
        if curr is None:
            rights += [None]
            continue
        rights += [curr.val]
        stack += [curr.right, curr.left]
        
    return rights == lefts  

def is_mirror(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    return left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

def isSymmetric(root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    return is_mirror(root.left, root.right)



def isSymmetric(root: Optional[TreeNode]) -> bool:
    queue = [root.left, root.right]
    while queue:
        left, right = queue.pop(0), queue.pop(0)
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        queue += [left.left, right.right, left.right, right.left]

    return True
    

