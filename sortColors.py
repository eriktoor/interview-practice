class Solution:
    """
https://leetcode.com/problems/sort-colors/

    """
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
        
        
    