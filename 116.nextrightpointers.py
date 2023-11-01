from collections import deque
from REF import Node

def connect(root: Node) -> Node:
    if root is None:
        return None
    lvl = 0
    start_idx = 0
    levels = []
    q = deque()
    q.append(root)
    nodes_traversed = 0
    while len(q) > 0:
        if nodes_traversed == start_idx:
            lvl += 1
            start_idx += 2 ** (lvl - 1) 
            levels.append([])
        curr = q.popleft()
        levels[-1].append(curr)
        nodes_traversed += 1
        if curr.left is not None:
            q.append(curr.left)
            q.append(curr.right)

    for level in levels:
        prev_node = None
        for node in level:
            if prev_node is not None:
                prev_node.next = node
            prev_node = node
    return root