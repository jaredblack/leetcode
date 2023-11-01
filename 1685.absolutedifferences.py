from itertools import accumulate

# prefix/postfix approach
def getSumAbsoluteDifferences(nums: list[int]) -> list[int]:
    prefix = list(accumulate(nums))
    prefix.insert(0, 0)
    suffix = list(accumulate(nums[::-1]))[::-1]
    l = len(nums)
    result = [0] * l

    for i, n in enumerate(nums):
        result[i] = abs(prefix[i] - n * i) + (suffix[i] - n * (l - i))

    return result



# standard dp approach
def getSumAbsoluteDifferences2(nums: list[int]) -> list[int]:
    result = [sum(nums) - nums[0] * len(nums)]
    for i in range(1,len(nums)):
        diff = nums[i] - nums[i-1]
        result.append(result[-1] + (diff * i) - diff * (len(nums) - i))

    return result

print(getSumAbsoluteDifferences2([2,3,5]))