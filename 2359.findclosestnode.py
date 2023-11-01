import math

def closestMeetingNode(edges: list[int], node1: int, node2: int) -> int:
    def find_all_reachable_nodes(node):
        reachable_set = set()
        dist_arr = [math.inf for _ in range(len(edges))]
        dist = 0
        while node != -1:
            if node in reachable_set:
                break
            reachable_set.add(node)
            dist_arr[node] = dist
            node = edges[node]
            dist += 1
        return reachable_set, dist_arr

    n1_reachable, n1_dist = find_all_reachable_nodes(node1)
    n2_reachable, n2_dist = find_all_reachable_nodes(node2)
    intersect = n1_reachable.intersection(n2_reachable)
    closest = next(iter(intersect)) if len(intersect) else -1
    for n in intersect:
        if max(n1_dist[n], n2_dist[n]) < max(n1_dist[closest], n2_dist[closest]) \
            or (max(n1_dist[n], n2_dist[n]) == max(n1_dist[closest], n2_dist[closest]) and n < closest):
            closest = n
    return closest

print(closestMeetingNode([1,2,-1],0,2))