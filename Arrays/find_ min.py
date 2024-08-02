# Return the minimum number in a list of numbers


def find_minimum(lst):
    min = float("inf")
    for num in lst:
        if num < min:
            min = num
    return min
