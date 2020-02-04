"""
Objective: s wordDict, return if s can be made of the elements in the wordDict 
*Can use each element multiple times 

Input: s = "leetcode", wordDict = ["code", "leet"]

Solution 1: look if each word in s and then decrease size of s 

Solution 2: 



leetcode.split(leet) -- >['code']

leetcode.split("tc") --> [lee, ode]

"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1) # dp[i] means s[:i+1] can be segmented into words in the wordDicts 
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j+1] in wordDict:
                    dp[j+1] = True
                    
        return dp[-1]

                
        
