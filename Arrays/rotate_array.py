# Given an array, rotate the array
def right_rotate(nums, k):
    # Determine rotation index
    if len(nums) == 0:
        k = 0  # If the list is empty, no rotation needed
    else:
        k = k % len(nums)  # Calculate effective rotation amount

    # Perform rotation by slicing the list
    rotated_list = nums[-k:] + nums[:-k]

    return rotated_list
