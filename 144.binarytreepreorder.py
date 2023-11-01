from REF import TreeNode
def preorderTraversal(root: TreeNode) -> list[int]:
    curr = root
    trav = []
    def traverse(node):
        if node is None:
            return
        trav.append(node.val)
        traverse(node.left)
        traverse(node.right)
    traverse(curr)
    return trav