class SolutionRobber:
    def robTopDownDP(self, hval): #TOP DOWN WITH MEMO 
        def helper(hval, i):
            if i < 0: return 0
            elif memo[i] >= 0: return memo[i]
            
            res = max(helper(hval, i-2) + hval[i], helper(hval, i -1))
            memo[i] = res 
            return res 
            
        memo = [-1 for i in range(len(hval) + 1)]
        return helper(hval, len(hval) - 1)

    def robTopDown(self, hval): #NO MEMO 
        def helper(hval, i):
            if i < 0: return 0

            res = max(helper(hval, i-2) + hval[i], helper(hval, i -1))

            return res 
            
        return helper(hval, len(hval) - 1)
    
    def rob(self, hval): #DP BOTTOM UP 
        if len(hval) == 0: return 0
        elif len(hval) == 1: return hval[0]
        elif len(hval) == 2: return max(hval[0], hval[1]) 
        
        memo = [0 for i in range(len(hval))]
        memo[0] = hval[0]
        memo[1] = max(hval[0], hval[1]) 
        
        for i in range(2, len(memo)): 
            memo[i] = max(hval[i] + memo[i-2], memo[i-1])
            
        return memo[-1]
  


class Solution_House_Rob_2:
    def rob(self, a: List[int]) -> int:
        n = len(a)
        if n==0:
            return 0
        if n==1:
            return a[0]
        if n==2:
            return max(a[0],a[1])
        if(n==3):
            return max({a[0],a[1],a[2]})
        
        dp1,dp2=[0]*n,[0]*n
        
        dp1[0],dp1[1] = a[0],max(a[0],a[1])
        for i in range(2,n-1):
            dp1[i] = max(dp1[i-2]+a[i], dp1[i-1])
        
        dp2[1],dp2[2] = a[1],max(a[1],a[2])
        for i in range(3,n):
            dp2[i] = max(dp2[i-2]+a[i], dp2[i-1])
        
        return max(max(dp1), max(dp2))