# Given two integer lists, nums1 and nums2,
# sorted in nondecreasing order. Merge nums1 and nums2 into a single list sorted in nondecreasing order.
# my solution is to iterate through both lists and add the smallest number to a new list until both lists are empty.
def merge_lists(nums1, nums2):
    merged = []
    while len(nums1) != 0 or len(nums2) != 0:
        if len(nums1) == 0:
            merged.append(nums2[0])
            nums2.pop(0)
        elif len(nums2) == 0:
            merged.append(nums1[0])
            nums1.pop(0)
        elif nums1[0] <= nums2[0]:
            merged.append(nums1[0])
            nums1.pop(0)
        else:
            merged.append(nums2[0])
            nums2.pop(0)

    return merged
