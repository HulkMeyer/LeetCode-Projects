# 🔁 LeetCode #9 – Palindrome Number

## Problem

![Palindrome Number Problem](Images/palindrome_number.png)

---

## 📝 Problem Summary

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

A number is a palindrome if it reads the same forwards and backwards (e.g. `121`, `1221`).  
Negative numbers are **not** palindromes.

---

## 📂 Scripts

| File | Language | Description |
|------|----------|-------------|
| `solution1_outside_in.py` | Python | Two-pointer approach starting from the outside edges, stepping inward until the pointers meet in the middle. |
| `solution2_middle_out.py` | Python | Two-pointer approach starting from the center, stepping outward to the edges. Handles even and odd length numbers differently. |

---

## 💡 Solution 1 – Outside In

**Logic:**
1. Reject negative numbers immediately.
2. Convert the integer to a string.
3. Place a `left` pointer at the first character and a `right` pointer at the last.
4. Compare the characters at both pointers — if they don't match, return `False`.
5. Step `left` forward and `right` backward, repeat until the pointers meet or cross.
6. If all pairs matched → Palindrome ✅

```python
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
```

---

## 💡 Solution 2 – Middle Out

**Logic:**
1. Reject negative numbers immediately.
2. Convert the integer to a string and find the midpoint.
3. **Even length** (e.g. `1221`) → start `left` and `right` on the two center characters.
4. **Odd length** (e.g. `12321`) → skip the true center character, start one step either side of it.
5. Compare the pair, then step `left` left and `right` right, repeat until the edges are reached.
6. If all pairs matched → Palindrome ✅

```python
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
```

---

## ✅ Examples

| Input | Output | Reason |
|-------|--------|--------|
| `121` | `true` | Reads the same forwards and backwards |
| `-121` | `false` | Negative numbers are never palindromes |
| `10` | `false` | Reads as `01` backwards — not the same |
| `1221` | `true` | Both outer and inner pairs match |

---

## 🏷️ Tags

`Math` · `Two Pointer` · `String` · `Easy`
