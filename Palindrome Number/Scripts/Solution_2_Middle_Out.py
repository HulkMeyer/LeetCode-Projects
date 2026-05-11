    """
    Given an integer x, return true if x is a palindrome, and false otherwise.
    Similar to last time checking for positive at the start, and then converting to string and checking from the middle outwards.
    Then calculate the middle.  starting from the middle and moving outwards check them pairwise.  If any pair doesn't match, return false. 
    If all pairs match, return true.
    """

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check if x is negative. If it is, it cannot be a palindrome.
        if x < 0:
            return False
        # Convert the integer to a string to check for palindrome properties.
        s = str(x)
        length = len(s)
        # Calculate the middle index of the string.
        mid = length // 2
        # Determine the left and right indices based on whether the length of the string is even or odd.
        if length % 2 == 0:
            # If the length is even, we set left and right to be around the middle point.
            left = mid - 1
            right = mid
        # If the length is odd, the middle character can be ignored, so we set left and right to be around the middle character.
        else:
            left = mid - 1
            right = mid + 1
        # Check characters from the middle outwards. If any pair of characters does not match, return False.
        while left >= 0 and right < length:
            if s[left] != s[right]:
                return False
            left -= 1
            right += 1

        return True