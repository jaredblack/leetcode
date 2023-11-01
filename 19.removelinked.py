class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    curr = head
    length = 0
    while curr:
        curr = curr.next
        length += 1

    if n == length:
        return head.next

    curr = head
    for i in range(0, length - n - 1):
        curr = curr.next

    if curr.next:
        curr.next = curr.next.next
    else:
        return None

    return head


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


linked = to_linked([1,2,3,4,5])
final = removeNthFromEnd(linked, 5)
print(to_arr(final))
