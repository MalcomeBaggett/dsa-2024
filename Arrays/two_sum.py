# Given a target number k and a list of numbers, write a function that returns two numbers from the list that add up to k.
# My solution: I will iterate through the list and for each number, I will calculate the difference between the target number and the current number.
# I will then check if the difference is in a dictionary. If it is, I will return the current number and the difference.
# If it is not, I will add the current number to the dictionary.


def find_sum(nums, k):
    num_dict = {}
    for num in nums:
        diff = k - num
        if diff in num_dict:
            return [num_dict[diff], num]
        else:
            num_dict[num] = num
