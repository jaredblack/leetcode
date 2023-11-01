from REF import ListNode
def detectCycle(self, head: ListNode) -> ListNode:
    curr = head
    nodes = set()
    while curr is not None:
        if curr in nodes:
            return curr
        nodes.add(curr)
        curr = curr.next
    return None
