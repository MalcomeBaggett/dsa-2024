# Given a list on integers remove all even numbers from the list and return the list with only odd numbers.
# Example: [1, 2, 3, 4, 5, 6, 7, 8, 9] -> [1, 3, 5, 7, 9]
# My solution: I will iterate through the list and add all odd numbers to a new list and return the new list.


def remove_even(lst):
    odd_list = []
    for num in lst:
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list
