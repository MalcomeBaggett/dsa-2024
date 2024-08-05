# Given a list nums, find the first nonrepeating integer in it.


def first_non_repeating(nums):
    num_dict = {}
    for i in nums:
        if i in num_dict:
            num_dict[i] += 1
        else:
            num_dict[i] = 1
    for i in nums:
        if num_dict[i] == 1:
            return i
    return 0
