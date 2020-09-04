class Solution:
    def lengthOfLISBS(self, nums: List[int]) -> int:
        def binarySearch(sub, val):
            lo, hi = 0, len(sub)-1
            while(lo <= hi):
                mid = lo + (hi - lo)//2
                if sub[mid] < val:
                    lo = mid + 1
                elif val < sub[mid]:
                    hi = mid - 1
                else:
                    return mid
            return lo
        
        sub = []
        for val in nums:
            pos = binarySearch(sub, val)
            if pos == len(sub):
                sub.append(val)
            else:
                sub[pos] = val
        return len(sub)
        
        
    def lengthOfLIS(self, nums: List[int]) ->int: #n^2
        
        if not nums: return 0 
        
        n = len(nums)
        lis = [1 for i in range(len(nums))]
        

        """
        1,6,2,3,4
        A
            B
        
        """
        
        for i in range (1 , n): 
            for j in range(0 , i): 
                if nums[i] > nums[j] and lis[i]< lis[j] + 1 : 
                    lis[i] = lis[j]+1
                    
        return max(lis)
    
    
    """
    
    State: 
        memoization, position, previous position 
    
    Base Case: 
        any value equals 1 
        
    Decisions: 
        choose one or don't chooes it (ie increment position or not)
    
    
    """
    
    def lengthOfLISBF(self, nums): #2^n
        
        def helper(nums, prev, curpos): 

            if curpos == len(nums):
                return 0
            taken = 0 
            if nums[curpos] > prev: 
                taken = 1 + helper(nums, nums[curpos], curpos + 1)
            nottaken = helper(nums, prev, curpos + 1)
            return max(taken, nottaken)
        
        return helper(nums, -1, 0)
    
    

            
            
            
            
        
