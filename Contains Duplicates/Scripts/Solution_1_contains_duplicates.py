    """
    To solve this problem first I want to sort the list of numbers.  Then I want to check the value above and 
    below it to see if they are the same.  If they are the same then I can return true.  If they are not the 
    same then I can move on to the next number and repeat the process until I have gone through the whole list.
    If I have gone through the whole list and have not found any duplicates then I can return false.
    """
    
    class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i-1]:
                return True
            elif nums[i] == nums[i+1]:
                return True
            else:
                return False
            
            
        """
        Presently does not work because it is only checking the first number and not the rest of the numbers in
        the list.
        """