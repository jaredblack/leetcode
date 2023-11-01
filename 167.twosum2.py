def twoSum(numbers: list[int], target: int) -> list[int]:
    p1 = 0
    p2 = len(numbers) - 1
    s = numbers[p1] + numbers[p2]
    while s != target:
        if s < target:
            p1 += 1
        elif s > target:
            p2 -= 1
        s = numbers[p1] + numbers[p2]
    return [p1 + 1, p2 + 1]

print(twoSum([5,25,75],100))