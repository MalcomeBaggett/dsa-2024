# Given an integer array nums, return true if any value appears more than once in the array,
#  otherwise return false.


def has_duplicate(nums):
    num_dict = {}
    for num in nums:
        if num in num_dict:
            return True
        num_dict[num] = num
    return False
