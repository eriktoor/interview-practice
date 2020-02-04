

def fib(n):
    if n == 0 or n == 1: 
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result

print(fib(7))

memo = {}
def fib_memo(n):
    if n in memo: 
        return memo[n]
    if n == 0 or n == 1: 
        result = 1
    else:
        result = fib_memo(n-1) + fib_memo(n-2)
    memo[n] = result
    return memo[n]

print(fib_memo(7))

def fib_dp(n): 
    dp = [0 for i in range(n + 1)]
    
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, len(dp)):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[-1]

print(fib_dp(7))
