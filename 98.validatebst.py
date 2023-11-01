import math
from leetcode.REF import TreeNode


def isValidBST(root: TreeNode) -> bool:
    def visit(node, lo=-math.inf, hi=math.inf):
        if node is None:
            return True
        if node.val >= hi or node.val <= lo:
            return False
        return visit(node.left, lo, node.val) and visit(node.right, node.val, hi)
    visit(root)