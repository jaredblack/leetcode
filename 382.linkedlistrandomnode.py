import random
from leetcode.REF import ListNode


class Solution:

    def __init__(self, head: ListNode):
        self.arr = []
        curr = head
        while curr != None:
            self.arr.append(curr)
            curr = curr.next

    def getRandom(self) -> int:
        return random.choice(self.arr)