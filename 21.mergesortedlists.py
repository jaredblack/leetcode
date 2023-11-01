from heapq import merge
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def get_val_or_

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    curr1 = list1
    curr2 = list2
    final_head = None
    if not list1 and not list2:
        return None
    elif list1 and not list2:
        return list1
    elif list2 and not list1:
        return list2
    if curr1.val < curr2.val:
        final_head = curr1
        curr1 = curr1.next
    else:
        final_head = curr2
        curr2 = curr2.next
    final_curr = final_head
    while curr1 != None or curr2 != None:
        if curr1 and curr2:
            if curr1.val < curr2.val:
                final_curr.next = curr1
                curr1 = curr1.next
            else:
                final_curr.next = curr2
                curr2 = curr2.next
        elif curr1:
            final_curr.next = curr1
            curr1 = curr1.next
        elif curr2:
            final_curr.next = curr2
            curr2 = curr2.next
        final_curr = final_curr.next
    return final_head

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

linked1 = to_linked([1])
linked2 = to_linked([2])
final = mergeTwoLists(linked1, linked2)
print(to_arr(final))