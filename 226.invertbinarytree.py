from leetcode.REF import TreeNode


def invertTree(self, root: TreeNode) -> TreeNode:
    def dfs(node):
        if node is None:
            return
        tmp = node.left
        node.left = node.right
        node.right = tmp
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return root