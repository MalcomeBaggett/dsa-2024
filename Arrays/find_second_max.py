# Given a list of nums return the second maximun number in the list.


def find_second_maximum(nums):
    max_num = float("-inf")
    second = float("-inf")
    for i in nums:
        if i > max_num:
            max_num = i

    for i in nums:
        if i > second and i != max_num:
            second = i
    return second
