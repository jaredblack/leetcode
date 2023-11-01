# Traverse through the tree in DFS order
# As soon as we're at an apple, return true to indicate that that branch needs to be traversed.
# As we're returning up from the recursion, add one to the path length if true was returned


from collections import defaultdict


def minTime(n: int, edges: list[list[int]], hasApple: list[bool]) -> int:

    edge_dict = defaultdict(list)
    for edge in edges:
        edge_dict[edge[0]].append(edge[1])
        edge_dict[edge[1]].append(edge[0])
        
    visited = [False for _ in range(n)]
    total_time = 0
    def check_for_apple(i):
        nonlocal total_time
        visited[i] = True
        worth_traversing = False
        for child in edge_dict[i]:
            if not visited[child]:
                is_apple_in_child_path = check_for_apple(child)
                if is_apple_in_child_path:
                    total_time += 1
                worth_traversing |= is_apple_in_child_path
        if hasApple[i]:
            return True
        return worth_traversing

    check_for_apple(0)
    return total_time * 2
    

print(minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False]))