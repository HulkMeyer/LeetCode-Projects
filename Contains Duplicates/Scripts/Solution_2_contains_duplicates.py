    """
    In this interation we will create a set and work through the nums set and if the value is not in the 
    new set we will add it, then more to the next set. 
    """
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
    