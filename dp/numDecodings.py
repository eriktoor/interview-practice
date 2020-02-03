class Solution:
    """
    https://leetcode.com/problems/decode-ways/
    1262
    
    [1,1,2,3,3]
    
    
    
    """
    def numDecodingsTimeOut(self, s): 
        if not s: return 0
        
        def helper(s):
            if not s: 
                return 1 
            
            if 0 < int(s[0]) < 10 and 10 <= int(s[0:2]) <= 26:
                return helper(s[1:]) + helper(s[2:])
            if 0 < int(s[0]) < 10: 
                return helper(s[1:])
            
            return 0 
                
                
        return helper(s)
    
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        dp = [0 for x in range(len(s) + 1)] 

        # base case initialization
        dp[0] = 1 
        dp[1] = 0 if s[0] == "0" else 1   #(1)

        for i in range(2, len(dp)): 
            # One step jump
            if 0 < int(s[i-1:i]) <= 9:    #(2)
                dp[i] += dp[i - 1]
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26: #(3)
                dp[i] += dp[i - 2]
        print(dp)
        return dp[-1]
    
    