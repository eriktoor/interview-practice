class Solution:

"""
https://leetcode.com/problems/longest-increasing-subsequence/submissions/


      A B
[1,10,2,3]

[1,2,2,3]

if nums[A] <= nums[B]: 
    dp[B] = max(dp[B], dp[A] + 1)

"""
    
    
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
    

            
            
            
            
class Solution:
    def lengthOfLongestSubstring1(self, s):
        dicts = {}
        maxlength = start = 0
        for i,value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        return maxlength
    
    def lengthOfLongestSubstring(self, s):
        if not s: return 0 
        
        if len(s) == len(set(s)): return len(s)
        
        maxVal = 1 
        
        for i in range(1, len(s)):
            for j in range(0, i): 
                if len(set(s[j:i])) == len(s[j:i]) and len(s[j:i]) > maxVal: 
                    maxVal = len(s[j:i])
        
        return maxVal 
                    
                
        

    """
3. Longest Substring Without Repeating Characters
Medium

7552

445

Add to List

Share
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    
    """