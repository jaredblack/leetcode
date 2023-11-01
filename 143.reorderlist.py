class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next

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

def reorderList(head: ListNode) -> None:
    curr = head
    stack = []
    l = 0
    while curr:
        l += 1
        stack.append(curr)
        curr = curr.next
    curr = head
    while curr:
        next = curr.next
        to_insert = stack.pop()
        curr.next = to_insert
        to_insert.next = next
        if len(stack) == l // 2:
            if l % 2 == 0:
                curr = next
            break
        curr = next
    curr.next = None

linked = to_linked([1,2,3,4,5])
reorderList(linked)
print(to_arr(linked))