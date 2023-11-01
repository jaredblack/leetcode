from leetcode.REF import TreeNode

# mock interview, topic exam (1/5)
def sumNumbers(root: TreeNode) -> int:
    def dfs(node, traversal):
        if node is None:
            return 0
        traversal.append(node.val)
        if node.left is None and node.right is None:
            ret = int("".join(map(str, traversal)))
            traversal.pop()
            return ret
        else:
            s = dfs(node.left, traversal) + dfs(node.right, traversal)
        traversal.pop()
        return s
    return dfs(root, [])