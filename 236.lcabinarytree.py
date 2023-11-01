from leetcode.REF import TreeNode

# topic exam trees (3/5)
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def dfs(node, trav, target_node):
        if node is None:
            return None
        trav.append(node)
        if node == target_node:
            return trav
        res = dfs(node.left, trav, target_node)
        if res:
            return res
        res = dfs(node.right, trav, target_node)
        if res:
            return res
        trav.pop()
    p_trav = dfs(root, [], p)
    q_trav = dfs(root, [], q)
    lastsame = None
    for pnode, qnode in zip(p_trav, q_trav):
        print(pnode, qnode)
        if pnode != qnode:
            return lastsame
        lastsame = pnode