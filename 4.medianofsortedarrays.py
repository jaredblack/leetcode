def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    def kth(a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2, len(b) // 2
        median_a, median_b = a[ia], b[ib]
        if ia + ib < k:
            if median_a > median_b:
                return kth(a, b[ib + 1:], k - ib - 1)
            else:
                return kth(a[ia + 1:], b, k - ia - 1)
        else:
            if median_a > median_b:
                return kth(a[:ia], b, k)
            else:
                return kth(a, b[:ib], k)

    l = len(nums1) + len(nums2)
    if l % 2 == 1:
        return kth(nums1, nums2, l // 2)
    else:
        return (kth(nums1, nums2, l // 2) + kth(nums1, nums2, l // 2 - 1)) / 2