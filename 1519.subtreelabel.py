from collections import defaultdict


def countSubTrees(n: int, edges: list[list[int]], labels: str) -> list[int]:
    subtree_match_counts = [0 for _ in range(n)]
    edge_dict = defaultdict(list)
    for edge in edges:
        edge_dict[edge[0]].append(edge[1])
        edge_dict[edge[1]].append(edge[0])

    visited = [False for _ in range(n)]
    def visit(node):
        visited[node] = True
        occurrences = [0 for _ in range(26)]
        for edge in edge_dict[node]:
            if not visited[edge]:
                descendent_occurrences = visit(edge)
                occurrences = [sum(x)
                            for x in zip(occurrences, descendent_occurrences)]
        occurrences[ord(labels[node]) - 97] += 1
        subtree_match_counts[node] = occurrences[ord(labels[node]) - 97]
        return occurrences

    visit(0)
    return subtree_match_counts


print(countSubTrees(4, [[0,2],[0,3],[1,2]], "aeed"))
