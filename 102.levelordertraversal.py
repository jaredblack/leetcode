class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode) -> list[list[int]]:
    if root is None:
        return []
    
    queue = []
    traversal = []
    
    queue.append((root, 0))
    
    while(len(queue) > 0):
        node, lvl = queue.pop(0)
        traversal.append((node.val, lvl))
        if node.left:
            queue.append((node.left, lvl+1))
        if node.right:
            queue.append((node.right, lvl+1))
    prev_lvl = -1
    fin = []
    for node, lvl in traversal:
        if lvl != prev_lvl:
            fin.append([])
        fin[-1].append(node)
    return fin
