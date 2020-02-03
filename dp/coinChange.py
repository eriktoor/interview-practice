class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0 
        # initiate
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            if coin < len(dp):
                dp[coin] = 1
        # iterate
        for s in range(len(dp)):
            subamount = dp[s]
            if subamount == amount+1:
                min_steps = amount+1
                for coin in coins:
                    if s-coin >= 0:
                        cur_min_steps = dp[s-coin]
                        if cur_min_steps < min_steps:
                            min_steps = cur_min_steps
                dp[s] = min_steps + 1
                
        return dp[-1] if dp[-1] < amount+1 else -1




"""
This code tells us the number of ways to make change
"""
def countOfWaysToMakeChange(arr_coins, num_coins, n): #top down m 

    # If n is 0 then there is 1 
    # solution (do not include any coin) 
    if (n == 0): 
        return 1

    # If n is less than 0 then no 
    # solution exists 
    if (n < 0): 
        return 0; 

    # If there are no coins and n 
    # is greater than 0, then no 
    # solution exist 
    if (num_coins <=0 and n >= 1): 
        return 0

    # count is sum of solutions (i)  
    # including S[m-1] (ii) excluding S[m-1] 
    return countOfWaysToMakeChange( arr_coins, num_coins - 1, n ) + countOfWaysToMakeChange( arr_coins, num_coins, n-arr_coins[num_coins-1] ); 




arr = [1, 2, 3] 
m = len(arr) #m is the number of coins 
print(countOfWaysToMakeChange(arr, m, 4)) #n is the value we are trying to create










def minChange(coins, value):
    res = []    
    def findMinChange(coins, value, num):
        if value == 0: 
            res.append(num)
        
        for i in coins: 
            if i <= value: 
                findMinChange(coins, value - i, num + 1)
        
        return res
    
    findMinChange(coins, value, 0)
    print(res)
    return min(res)
    



arr = [1, 2, 3] 
print(minChange(arr, 5)) #n is the value we are trying to create



def minChange(coins, value):
    res = []
    memo = [value + 1 for i in range(value + 1)]
    def findMinChange(coins, value, num):
        if value in memo: 
            return memo[value]
        
        if value == 0: 
            res.append(num)
        
        for i in coins: 
            if i <= value: 
                dp = findMinChange(coins, value - i, num + 1)
                memo[i] = dp
        
        return res
    
    findMinChange(coins, value, 0)
    print(res)
    return min(res)
    



arr = [1, 2, 3] 
print(minChange(arr, 5)) #n is the value we are trying to create