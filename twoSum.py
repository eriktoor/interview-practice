class Solution2Sum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for index, val in enumerate(nums):
            seen[val] = index
        
        for index, val in enumerate(nums):
            if target - val in seen:
                if index != seen[target-val]: return [index, seen[target-val]]
                
from collections import Counter
class Solution3Sum:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
     
        if len(nums) < 3: return []

        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return map(list, res)

"""

https://www.pramp.com/challenge/gKQ5zA52mySBOA5GALj9

https://leetcode.com/problems/4sum/

"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """       
        
        p = c = 0
        
        p2 = len(nums) - 1
        
        while c <= p2:
            if nums[c] == 0:
                nums[c], nums[p] = nums[p], nums[c]
                p += 1 
                c += 1
            elif nums[c]== 2:
                nums[c], nums[p2] = nums[p2], nums[c]
                p2 -= 1
            else:
                c += 1
        
        
        
        
     