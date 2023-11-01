from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderBottom(root: TreeNode) -> list[list[int]]:
    q = deque()
    if root:
        q.append((root, 0))
    traversal = []
    prev_lvl = -1
    while len(q):
        n, lvl = q.popleft()
        if prev_lvl != lvl:
            traversal.append([])
        traversal[-1].append(n.val)
        if n.left:
            q.append((n.left, lvl + 1))
        if n.right:
            q.append((n.right, lvl + 1))
        prev_lvl = lvl
    return reversed(traversal)