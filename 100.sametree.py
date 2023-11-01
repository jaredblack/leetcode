# BFS version to practice BFS. DFS (recursive) solution is much cleaner

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    qqueue = deque()
    pqueue = deque()
    qqueue.append(q)
    pqueue.append(p)

    while len(qqueue) or len(qqueue):
        pnode = pqueue.pop()
        qnode = qqueue.pop()

        if pnode == None and qnode == None:
            continue
        
        if ((pnode == None) != (qnode == None)) or pnode.val != qnode.val:
            return False

        if qnode != None: 
            qqueue.append(qnode.left)
            qqueue.append(qnode.right)  
        if pnode != None:
            pqueue.append(pnode.left)
            pqueue.append(pnode.right)  
        
    return True