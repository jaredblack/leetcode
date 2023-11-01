from collections import deque
from leetcode.REF import TreeNode


def zigzagLevelOrder(root: TreeNode) -> list[list[int]]:
    if root is None:
        return []
    q = deque()
    q.appendleft((root, 0))
    traversal = []
    prev_lvl = -1
    while len(q):
        curr = q.pop()
        node, lvl = curr
        if lvl > prev_lvl:
            if prev_lvl % 2 == 1 and prev_lvl > 0:
                traversal[-1] = list(reversed(traversal[-1]))
            traversal.append([])
            prev_lvl += 1
        traversal[-1].append(node.val)
        print(lvl)
        lvl += 1
        first, second = node.left, node.right
        if first is not None:
            q.appendleft((first, lvl))
        if second is not None:
            q.appendleft((second, lvl))
    if len(traversal) % 2 == 0:
        traversal[-1] = list(reversed(traversal[-1]))
    return traversal