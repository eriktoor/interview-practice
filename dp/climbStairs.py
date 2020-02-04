class Solution:
    def climbStairs(self, n): 
        memo = [0 for i in range(n + 1)]
        memo[0] = 1
        memo[1] = 1
        for i in range(2, len(memo)):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[-1]
    
    def climbStairsTopDownMemo(self, n:int) -> int:
        memo = {}
        def helper(i ,n):
            if i in memo:
                return memo[i]
            if i == 0:
                return 1 
            elif i < 0: 
                return 0 

            memo[i] = helper(i-1, n) + helper(i-2, n)
            return memo[i]
        return helper(n, n)
