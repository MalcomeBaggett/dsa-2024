# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.


def is_palindrome(s):
    new_str = ""
    for char in s:
        if char.isalnum():
            new_str += char.lower()
    left = 0
    right = len(new_str) - 1
    while left < right:
        if new_str[left] != new_str[right]:
            return False
        left += 1
        right -= 1
    return True
