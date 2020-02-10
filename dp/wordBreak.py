"""
Objective: s wordDict, return if s can be made of the elements in the wordDict 
*Can use each element multiple times 

Input: s = "leetcode", wordDict = ["code", "leet"]

Solution 1: look if each word in s and then decrease size of s 

Solution 2: 



leetcode.split(leet) -- >['code']

leetcode.split("tc") --> [lee, ode]

"""


"""

https://leetcode.com/problems/word-break/submissions/

https://leetcode.com/problems/word-break-ii/discuss/44368/Python-easy-to-understand-solution-(DP%2BDFS%2BBacktracking).

Approaches: 

Approach 0: Top Down 

Try each value in word dict until we approach word = ""

Time: O(n^n)

Approach 1: Top Down with memoization 

State: 
    word, location in word given by a start and end pointer

    l e e t c o d e 
    A
          B     

Base Cases: 
    if string is empty: return True 
    if slice of s in dict: return True 
    if slice of s in memo: return memo[slice of s]

Decisions: 
    Try all of the start end combos until you find one that works 

Time: O(n^2) because we are memoizing every possible substring

Approach 1: Bottom Up with Memoization 

dp[0] = True 

after if dp[i] is true and slice of s in worddict: 
    dp[j+1] = True where j is the end of the word
    
return dp[-1]


Time: O(n^2)

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

    

    
    def wordBreak(self, s, dict):
        dict = set(dict)
        start = 0
        end = len(s)-1
        memo = {}
        return self._wordBreak(s, dict, start, end, memo)
        
    def _wordBreak(self, s, dict, start, end, memo):
        if s[start:end+1] in memo:
            return memo[s[start:end+1]]
        elif s[start:end+1] in dict:
            memo[s[start:end+1]] = True
            return True
        for i in range(start, end):
            if s[start:i+1] in dict and self._wordBreak(s, dict, i+1, end, memo):
                return True
        memo[s[start:end+1]] = False
        return False
                
        


