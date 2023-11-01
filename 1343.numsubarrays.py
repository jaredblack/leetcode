def numOfSubarrays(arr: list[int], k: int, threshold: int) -> int:
    total_subarrays = 0
    subtotal = sum(arr[:k])
    if subtotal / k >= threshold:
        total_subarrays += 1
    for i in range(k, len(arr)):
        subtotal -= arr[i-k]
        subtotal += arr[i]
        if subtotal / k >= threshold:
            total_subarrays += 1
    return total_subarrays

print(numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))