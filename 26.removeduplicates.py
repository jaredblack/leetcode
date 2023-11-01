

def removeDuplicates(nums: list[int]) -> int:
    unique_ind = 0
    max = nums[-1]
    if len(nums) == 1:
        return 1
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            for j in range(unique_ind, len(nums)):
                if nums[j] > nums[i-1]:
                    unique_ind = j
                    nums[i] = nums[unique_ind]
                    break
        if nums[i] == max:
            break
    print(nums)
    return nums.index(max)+1

print(removeDuplicates([1,2]))