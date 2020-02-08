class Solution:
    """
    
    Approaches: 
    
    Approach 1: Top Down Brute Force 
    
    State: 
        - step I am on 
        - total number of ways 
    
    Base Case:
        - if n == 0: return numWays += 1 
        - if n < 0: return 
    
    Decisions: 
        - take one step --> climbStairsHelper( n-1)
        - take two steps --> climbStairsHelper( n-2)
        
        
    Pseudocode - code 
    
    if n == 0: return 1 
    if n < 0: return 0 
    return climbStairs(n-1) + climbStairs(n-2)
        
    Time: O(2^n), Space: O(2^n) calls on the call stack to climbStairsHelper
    
    ## pluses of this approach is that it's a three liner 
    
    Decision Tree   2 
                   / \
                cs(1) cs(0)
                /  \
             cs(0) cs(-1) 
             
    ## negatives is that we recompute subproblems 
    
    Approach 2: Top Down with Memoization (Dynamic Programming)
    
    Utilize same state, base case, decisions from lines 10 to 21 
    
    Store the cases to the subproblem in a DP dict 
    
    Time: O(n), Space: O(n) and n calls to the call stack 
    
    Approach 3: Bottom up with Memoization using a DP array 
    
    store base cases at index 0 and index 1 of the array and iterate through the array
    
    Pseudocode 
    
    init memo array 
    memo[0] = 0
    memo[1] = 1 
    
    iterate over memo: 
        each memo[i] = memo[i-1] + memo[i-2]
    
    return memo[-1]
    
    Time: O(n), Space: O(n) 
    
    """

    
    
    def climbStairs(self, n): 
        """
        @desc given a staircase of n height, how many ways are there to reach the top if you can go 1 or 2 steps at a time
        @args
            @arg1 n the size of the staircase
        @return numWays, an int representing the number of ways you can climb up the n stairs
        """
        if n == 0: return 1 
        if n < 0: return 0 
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    def climbStairs(self, n): 
        """
        @desc given a staircase of n height, how many ways are there to reach the top if you can go 1 or 2 steps at a time
        @args
            @arg1 n the size of the staircase
        @return numWays, an int representing the number of ways you can climb up the n stairs
        """
        memo = {}
        def helper(i ,n):
            if i in memo: return memo[i]
            if i == 0: return 1 
            elif i < 0: return 0 

            subproblem = helper(i-1, n) + helper(i-2, n)
            memo[i] = subproblem 
            return memo[i]
        
        return helper(n, n)
    def climbStairs(self, n): 
        """
        @desc given a staircase of n height, how many ways are there to reach the top if you can go 1 or 2 steps at a time
        @args
            @arg1 n the size of the staircase
        @return numWays, an int representing the number of ways you can climb up the n stairs
        """
        memo = [0 for i in range(n + 1)]
        memo[0] = 1
        memo[1] = 1
        
        for i in range(2, len(memo)): 
            memo[i] = memo[i-1] + memo[i-2]
        return memo[-1]
    
    
    def climbStairsBottomUp(self, n): 
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








"""

https://www.youtube.com/watch?v=5o-kdjv7FD0&t=1030s

Recursive Staircase Problem with set of stairs 

Approaches: 

Approach 1: Top Down 

State: 
    - steps, n
    - which step we are on * (currStep)
Base Case: 
    - if currStep == 0: we found a way
    - if currStep < 0: we didn't find a way 
Decisions: 
    - make the steps climbStairs(steps, n - i for i in steps)
    
steps = {0 , 1}, n = 2 

Decision Tree for line 15
      cs 2 
     /   \
  cs 1   cs 0
   /  \
 cs -1 cs 0
 
 ** we are recalculating subproblems but we get a really simple solution

"""

def climbStairsSet(steps, n): 
    """
    @desc given a set steps of the types of way you can climb stairs climb the stairs
    @args
        @arg1 steps, a set of the ways you can climb the stairs
        @arg2 n, the number of steps
    @return ret, an int representing the number of ways
    """
    if n == 0: return 1 
    if n < 0: return 0 
    
    numWays = 0

    for i in steps: 
        if n - i >= 0: 
            numWays += climbStairsSet(steps, n - i)
    
    return numWays
    
steps = {1, 2}
n = 2
print(climbStairsSet(steps, n))

def climbStairsSet(steps, n): 
    """
    @desc given a set steps of the types of way you can climb stairs climb the stairs
    @args
        @arg1 steps, a set of the ways you can climb the stairs
        @arg2 n, the number of steps
    @return ret, an int representing the number of ways
    """
    if n == 0: return 1 
    nums = [0 for i in range(n + 1)]
    nums[0] = 1
    
    for i in range(1, len(nums)): 
        total = 0 
        for j in steps: 
            if n - j >= 0: 
                total += nums[i-j]
        nums[i] = total
    return nums[n]

steps = {1, 2}
n = 2
print(climbStairsSet(steps, n))

    