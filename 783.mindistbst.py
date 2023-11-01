from REF import TreeNode

def minDiffInBST(root: TreeNode) -> int:
    min_diff = 100000
    def dfs(node, path):
        nonlocal min_diff
        for n in path:
            diff = abs(node.val - n)
            if diff < min_diff:
                min_diff = diff
        path.append(node.val)
        if node.left:
            dfs(node.left, path)
        if node.right:
            dfs(node.right, list(path))
    dfs(root, [])
    return min_diff