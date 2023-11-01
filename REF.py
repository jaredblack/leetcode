class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Linked Lists
def to_linked(list):
    if len(list) == 1:
        return ListNode(list[0], None)
    else:
        return ListNode(list[0], to_linked(list[1:]))

def to_arr(head: ListNode):
    curr = head
    arr = []
    while curr != None:
        arr.append(curr.val)
        curr = curr.next
    return arr

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next