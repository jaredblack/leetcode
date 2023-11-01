# this solution is even more inefficient than it needs to be (whatever I guess)
# a better way to think about it: 
#  - run DFS just once from the root
#  - at each iteration of the DFS, you have two options: add the next number, or don't
#  - each level of the DFS tree corresponds to each number in the input array 
#  - run the dfs on each of those options. once you get through the whole tree you'll have all the subsets.
# this gets rid of a lot of the duplicate work.
def subsets(nums: list[int]) -> list[list[int]]:
    subs = {frozenset()}

    def dfs(trav):
        subs.add(trav)
        if len(trav) == len(nums):
            return
        for k in nums:
            if k not in trav:
                dfs(frozenset((*trav, k)))
    for n in nums:
        dfs(frozenset((n,)))
    return subs


print(subsets([1, 2, 3]))
