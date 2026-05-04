class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}

        for i, x in enumerate (nums):
            need = target - x
            if need in checked:
                return[checked[need],i]
            checked[x] = i