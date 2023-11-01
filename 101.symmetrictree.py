from REF import TreeNode
def isSymmetric(root: TreeNode) -> bool:
    lstack = [root.left]
    rstack = [root.right]
    while len(lstack) and len(rstack):
        l = lstack.pop()
        r = rstack.pop()
        if ((l is None) ^ (r is None)):
            return False
        if l is None:
            continue
        if l.val != r.val:
            return False
        lstack.append(l.left)
        lstack.append(l.right)
        rstack.append(r.right)
        rstack.append(r.left)
    return True