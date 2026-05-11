    """
    To check is a number is a palindrome you first need to check and see if it is positive.
    Then you want the first and last numbers to be the same and work toward the center from
    wanting each pair to be the same.  So starting from the ends and working in a pair at a time
    If the pairs are the same then you can continue to the next pair.  If you get to the middle
    and all pairs are the same, then the number is a palindrome.
    """
    
    class Solution:
    def isPalindrome(self, x: int) -> bool:
        #  Check if number is positive - Only Positive numbers can be a palindromes
        if x < 0:
            return False
        # Convert the number to a string so we can check the first and last characters
        s = str(x)
        # Get the length of the string so we can use it to find the last character and to know when we have reached the middle
        length = len(s)

        # Set two pointers, one at the beginning of the string and one at the end of the string.  We will use these pointers to check the characters at the beginning and end of the string and move them towards the center as we check each pair of characters.
        left = 0
        right = length - 1
        #  Loop through the string until the left pointer is less than the right pointer.  This means we have not yet reached the middle of the string.  If the characters at the left and right pointers are not the same, then we can return false because it is not a palindrome.  If they are the same, then we can move the left pointer to the right and the right pointer to the left and continue checking the next pair of characters.
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True