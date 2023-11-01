from REF import TreeNode

# Tree topic exam (2/5)
# did it in like 10 minutes
def pathSum(root: TreeNode, targetSum: int) -> list[list[int]]:
    good_paths = []
    def dfs(node, trav, curr_sum):
        if node is None:
            return
        trav.append(node.val)
        curr_sum += node.val
        if curr_sum == targetSum and node.left is None and node.right is None:
            good_paths.append(list(trav))
        else: 
            dfs(node.left, trav, curr_sum)
            dfs(node.right, trav, curr_sum)
        trav.pop()
    dfs(root, [], 0)
    return good_paths

