# Cracking the Coding Interview 1.1
# The CtCI version of the problem is determing if a string has all unique characters. In that case 
# another good solution is to create a bit vector that maps each ASCII code to whether it occurs (len 128)

# my initial O(n) solution using additional set
def containsDuplicate(nums: list[int]) -> bool:
    nums_set = set(nums)
    return len(nums_set) != len(nums)
