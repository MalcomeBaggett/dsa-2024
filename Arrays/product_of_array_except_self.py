# You’re given an integer array, nums. Return a resultant array product so that product[i]
# is equal to the product of all the elements of nums except nums[i].


def find_product(nums):
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    # iterate through the array in reverse
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res
