from REF import TreeNode
def inorderTraversal(root: TreeNode) -> list[int]:
    def inorder(node, traversal):
        if node is None:
            return traversal
        inorder(node.left, traversal)
        traversal.append(node.val)
        inorder(node.right, traversal)
        return traversal

    return inorder(root, [])