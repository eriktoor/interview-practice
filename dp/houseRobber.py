class Solution:
    
    """
    
    Approaches:
    
    Approach 1: Top Down 
    
    State: 
        - hval 
        - currentHouse * (value you are changing)
    
    Base Cases: 
        - if there are no houses: can't pick anything 
        - if there is 1 houses: pick it 
        - if there is 2 houess: pick the max value house
        
    Decisions: 
        - pick the current house and the house two houses before 
        - pick the house 1 before 
    
    Pseudocode: 
    def rob(self, hval):
        def helper(hval, i):
            if i < 0: return 0 
            
            # pick_house = hval[i] + helper(hval, i - 2)
            # pick_house_before = helper(hval, i - 1)
            # return max(pick_house, pick_house_before)
            return max(hval[i] + helper(hval,i-2), helper(hval, i-1))
        
    return helper(hval, len(hval)-1)
    

    Time: O(2^n), Space: O(2^n) calls on the call stack 
    
    Decision Tree
    [1,2,3,1]
                    h(hval, 4)
                   /         \ 
         h(hval, 3)         h(hval, 2) + hval[4]
        /       \                 /             \
h(hval, 2)  h(hval,1) +hval[3]  h(hval, 1)   h(hval, 0) + hval[2]



    Approach 1: Top Down with Memoization 
    
    Same exact approach, but storing the results of completed subproblems 
    
    
    Pseudocode: 
    def rob(self, hval):
        memo = {}
        def helper(hval, i):
            if i in memo: return memo[i]
            if i < 0: return 0 
            
            # pick_house = hval[i] + helper(hval, i - 2)
            # pick_house_before = helper(hval, i - 1)
            # return max(pick_house, pick_house_before)
            memo[i] =  max(hval[i] + helper(hval,i-2), helper(hval, i-1))
            return memo[i]
    return helper(hval, len(hval)-1)
    


    """ 
    
    
    def robTopDownDP(self, hval): 
        def helper(hval, i):
            if i < 0: return 0
            elif memo[i] >= 0: return memo[i]
            
            #res = max(helper(hval, i-2) + hval[i], helper(hval, i -1))
            #memo[i] = res 
            #return res 
            memo[i] = max(helper(hval, i-2) + hval[i], helper(hval, i -1))
            return memo[i]
        
        memo = [-1 for i in range(len(hval) + 1)]
        return helper(hval, len(hval) - 1)

    def robTopDown(self, hval): 
        def helper(hval, i):
            if i < 0: return 0

            res = max(helper(hval, i-2) + hval[i], helper(hval, i -1))

            return res 
            
        return helper(hval, len(hval) - 1)
    
    def robBottomUp(self, hval): 
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
