from leetcode.REF import TreeNode


def postorderTraversal(root: TreeNode) -> list[int]:
    trav = []
    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        traverse(node.right)
        trav.append(node.val)
    traverse(root)
    return trav