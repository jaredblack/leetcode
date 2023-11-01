class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# with memory allocation
def hasCycle(self, head: ListNode) -> bool:
    node = head
    nodes = set()
    while node:
        if node in nodes:
            return True
        else:
            nodes.add(node)
            node = node.next
    return False