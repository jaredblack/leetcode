import collections
import math


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    insert_pos = len(nums1) - 1
    n1p = m - 1
    n2p = n - 1

    while insert_pos >=  0:
        to_insert = 0

        if not n1p < 0 and (n2p < 0 or nums1[n1p] > nums2[n2p]):
            to_insert = nums1[n1p]
            n1p -= 1
        else:
            to_insert = nums2[n2p]
            n2p -= 1
        nums1[insert_pos] = to_insert
        insert_pos -= 1

nums1 = [2,0]
nums2 = [1]

merge(nums1, 1, nums2, 1)
print(nums1)