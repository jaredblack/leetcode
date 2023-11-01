class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: TreeNode) -> int:
    max_len = 0
    def find_subtree_length(node):
        nonlocal max_len
        left_len = find_subtree_length(node.left) if node.left else 0
        right_len = find_subtree_length(node.right) if node.right else 0
        if left_len + right_len > max_len:
            max_len = left_len + right_len
        return max(left_len, right_len) + 1
        
    find_subtree_length(root)
    return max_len