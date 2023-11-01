def maxDepth(root: TreeNode) -> int:
    def dfs(node, cd):
        if node is None:
            return cd
        cd += 1
        return max(dfs(node.left, cd), dfs(node.right, cd))

    dfs(root, 0)
        