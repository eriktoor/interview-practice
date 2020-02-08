class SolutionMaxSum:
    
    """
    
    https://leetcode.com/problems/maximum-subarray/submissions/

    Approaches: 
    
    Approach 1: Keep a running sum 
    
    State: 
        Pointers 
    Base Case: 
        if there are no numbers return 0
    Decisions: 
        if currentSum + val[i] > val[i] pick that else pick other 
        always store the best currentSum in best sum 
    
    
    [-2,1,-3,4,-1,2,1,-5,4],
      A
      
    bestSum = firstVal
    currentSum = firstVal 

    # two values that could be greater than current sum, current_sum + val[A] or val[A]
    currentSum = max(val[A] + currentSum, val[A])
    
    #bestSum is always the maximum of the current sum and itself 
    
    increment A
    

    result: 6
    
    """
    
    def maxSubArray(self, nums: List[int]) -> int:
        """
        @desc find the max contiguous subarray inside an array nums
        @args
            @arg1 nums, a list of integers 
        @return maxSum, an int representing the size of the max sum subarray         
        """
        if len(nums) == 0: return 0 
        
        maxSum = nums[0]
        current = nums[0]
        
        for i in range(1, len(nums)): 
            current = max(nums[i] + current, nums[i])

            maxSum = max(current, maxSum)
            
        return maxSum
        


class SolutionMaxProduct:
    
    
    """
    
    Approaches:
    
    Approach 1: Keep a running product
    
    State: 
        iterator that will iterate over nums
    Base Case:
        if the array is empty return 0 
    Decisions: 
        #choice being made is to include all of the previous calculations in the max or not 
        currentProd = max(currentProd * val[iterator], val[iterator])
        maxProd = max(currentProd, maxProd)
    
    
    """
    
    def maxProduct(self, nums: List[int]) -> int:
        """
        @desc find the largest product of a continuous subarray 
        @args
            @arg1 nums a list of integers 
        @return maxProduct, an int representing the larget product of a continuous subarray in nums 
        """
        if not nums: return 0 
        
        curr_max = nums[0]
        curr_min = nums[0]
        final_max = nums[0]
        
        for i in range(1,len(nums)):
            temp = curr_max
            curr_max = max(max(curr_max*nums[i],curr_min*nums[i]),nums[i])
            curr_min = min(min(temp*nums[i],curr_min*nums[i]),nums[i])
            
            if(curr_max > final_max):
                final_max = curr_max
            
        return final_max