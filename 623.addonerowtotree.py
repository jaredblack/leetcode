from leetcode.REF import TreeNode


def addOneRow(root: TreeNode, val: int, depth: int) -> TreeNode:
    def add_row(node, curr_depth):
        if node is None:
            return
        if curr_depth < depth:
            add_row(node.left, curr_depth + 1)
            add_row(node.right, curr_depth + 1)
            return
        left_sub = node.left
        right_sub = node.right
        node.left = TreeNode(val, left_sub)
        node.right = TreeNode(val, None, right_sub)
    
    if depth == 1:
        root = TreeNode(val, root)
    else:
        add_row(root, 2)
    return root