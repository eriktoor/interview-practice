"""
Examples: 

[1,5,11,5] --> [1,5,5], [11]
True because sets are equal

[1,5,11,4] --> [1,5,4], [11]
False false 

Approaches: 

Approach 1: Simulating Picking and Not Picking Each Value 

Time: O(2^n)

Approach 2: Picking and Not Picking with Memoization

    State:  
        target, index, memoized array or dictionary 

    Base Cases: 
        if choice in memo: return memo[choice]
        if sum(arr) % 2 != 0: return False 
        if target - value == 0: return True 

    Decisions 
        take_the_number = helper(arr, index+1, target-arr[index])
        skip_the_number = helper(arr, index+1, target)



"""

class Solution:
    
    def canPartition(self, nums):
        """
        @desc given an array find if the array can be partitioned into two subsets such that the sum of the subsets are equal
        @args
            @arg1 arr of positive nums 
        @ret a boolean of whether this is possible or not
        
        @example invocations
        >>>canPartition(self, [1,5,11,5]) # sets should be [1,5,5], [11]
        True 
        >>>canPartition(self, [1,5,11,4]) # closest set would be [1,5,4], [11], but aren't equal
        False 
        """                
        #self.d = {}
        d = {}
        total = sum(nums)
        if total %2:
            return False
        
        return self.find_sum(nums, 0, 0, total//2, d)
        
    def find_sum(self, nums, index, current_sum, total, d):
        if index >= len(nums):
            return False        
        if current_sum == total:
            return True
        if not nums or current_sum > total:
            return False
        if (len(nums), current_sum) in d:
            return False
        
        found = self.find_sum(nums, index +1, current_sum+nums[index], total, d) or self.find_sum(nums, index + 1, current_sum, total, d)
        
#         take_number = self.find_sum(nums, index +1, current_sum+nums[index], total, d)
#         skip_number = self.find_sum(nums, index + 1, current_sum, total, d)
        
#         found = take_number or skip_number
                
        if found: return True 
            
        d[(len(nums), current_sum)] = False
        return False