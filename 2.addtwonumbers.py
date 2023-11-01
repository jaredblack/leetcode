# Second solution is probably more efficient/the "right" solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_linked(list):
    if len(list) == 1:
        return ListNode(list[0], None)
    else:
        return ListNode(list[0], to_linked(list[1:]))

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    n1_arr = []
    n2_arr = []
    curr = l1
    while curr != None:
        n1_arr.append(curr.val)
        curr = curr.next 
    curr = l2
    while curr != None:
        n2_arr.append(curr.val)
        curr = curr.next
    n1 = int(''.join(reversed([str(x) for x in n1_arr])))
    n2 = int(''.join(reversed([str(x) for x in n2_arr])))
    s = n1 + n2

    sumstr = str(s)
    head = ListNode()
    curr = None
    for c in reversed(sumstr):
        if curr == None:
            curr = head
        else:
            curr.next = ListNode()
            curr = curr.next
        curr.val = int(c)

    return head

def addTwoNumbers2(l1: ListNode, l2: ListNode) -> ListNode:
    res = None
    curr = None
    carry = False
    while l1 or l2:
        new_node = (l1.val if l1 else 0) + (l2.val if l2 else 0) + (1 if carry else 0)
        carry = new_node > 9 
        if carry:
            new_node -= 10
        if curr:
            curr.next = ListNode(new_node)
            curr = curr.next
        else:
            curr = ListNode(new_node)
            res = curr
        # print(new_node, end='')
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return res
        



print(addTwoNumbers2(to_linked([2,4,3]), to_linked([5,6,4])))