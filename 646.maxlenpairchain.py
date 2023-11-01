# sorting topic exam 1/5
def findLongestChain(pairs: list[list[int]]) -> int:
    # if this is too slow, may want to sort reversed and then iterate backwards for less expensive removal
    # better yet, a linked list!
    pairs.sort(key=lambda x: x[1])

    curr_end = -1001
    old_len, new_len = -1, 0
    while new_len > old_len:
        old_len = new_len
        for pair in pairs:        
            if pair[0] > curr_end:
                new_len += 1
                pairs.remove(pair)
                curr_end = pair[1]
                break
        else:
            break
    return new_len

print(findLongestChain([[1,2],[2,3],[3,4]]))