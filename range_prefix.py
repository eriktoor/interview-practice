"""
Smallest range 2
"""


class Solution:
    """
    Approaches 

    nums = [0,10]
    k = 2 

    output is 6 
    this is because we can add 2 to index 0 and subtract 2 from index 1 
    then our arr is [2,8] and the range is 6 

    Approach 1: get the average and increment everything towards that average 
    - get average 
    - loop over and increment everything towards that average 


    nums_average = sum(nums) / len(nums)


    """

    def smallestRangeII(self, A: List[int], K: int) -> int:
        """
        @desc given an arr and integer change all nums to be nums[i] + or - k to ensure the smallest range
        @args
            @arg1 nums a list of integers
            @arg2 k an integer 
        @return score, the min score of nums after changing the values at each index 
        """
        A.sort()
        mi, ma = A[0], A[-1]
        ans = ma - mi
        for i in range(len(A) - 1):
            a, b = A[i], A[i+1]
            ans = min(ans, max(ma-K, a+K) - min(mi+K, b-K))
        return ans


"""
Range Addition
ans is the array that will store the answer
Step 1: For every update with startIdx, endIdx, and incrementValue:
ans[startIdx] += incrementValue
ans[endIdx + 1] -= incrementValue (if endIdx + 1 is not out of range. If it is out of range, we don't do anything)
Step 2: At the end, we iterate the array from index 1 (0-based indexing), and set:
ans[i] += ans[i-1]. This is basically prefix-sum
"""


def range(length, updates):
    ans = [0] * length
    for start, end, value in updates:
        ans[start] += value
        end += 1
        if end < len(ans):
            ans[end] -= value

    for i in range(1, len(ans)):
        ans[i] += ans[i-1]

    return ans


"""
DIVISIBLE BY K
"""


class Solution:

    """

    Input: nums = [4,5,0,-2,-3,1], k = 5
    Output: 7
    Explanation: There are 7 subarrays with a sum divisible by k = 5:
    [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

    Approaches: 

    Thoughts: this is combination sum with divisbility and with contiguous numbers 

    Approach 1: Find all subarray sums then check which are divisble with K 

    Sliding window of 1... N 

    [4,5,0,-2,-3,1] --> 5

    while window > 0: 
        for i in range(start_idx, len(nums) - window):
            check if it is divisble and if this is the case incrememt

    TLE if you have to recalcualte the amount each time 

    """

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        @desc given an arr of nums and int, find the number of non-empty subarray sumps divisble by k
        @args
            @arg1 nums a list of ints
            @arg2 k an int
        @return divisbleByK, an int explaining how many (contiguous) subarray sums are divisble by k 
        """
        divisbleByK = 0
        n = len(nums)
        window = len(nums)

        while window > 0:
            for start_idx in range(0, (n - window)+1):
                val = sum(nums[start_idx:start_idx+window])
                if val % k == 0:
                    divisbleByK += 1
            window -= 1

        return divisbleByK

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        memo = [0] * k
        memo[0] = 1
        ans = 0
        for i in nums:
            prefix_sum = (prefix_sum + i) % k
            ans += memo[prefix_sum]
            memo[prefix_sum] += 1

        return ans


"""
Input: 
nums = [5], 
k = 9
Output: 0

n, window = 1, 1
start_idx in (0, (1-1)+1)

sum(nums[0:0+1])

"""

"""
Using Prefix Sum 

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7

memo = [1,0,0,0,2,0,2,0]

for each val,
    if the curr sum % val is 0, 
        add ans += memo[0]
    memo[curr_sum % val] += 1 
return ans \

curr_sum = 
ans = 5


"""


"""
Subarray Sum Equals K
"""


class Solution:

    """

    Approaches: 

    Approach 1: sliding window size n decreasing to size zero and iterating over arr from start to n+1-window 
    1. have a window size n 
    2. while the window is > 0 
    3. iterated from (0,n-len window) 
    4. if sum is == k: ans += 1 

    Time: O(N * (N+1) / 2) or (n^2 + n) / 2 , Space: O(1)

    Approach 2: using prefix sum 

    [1,2,3]
    [1,3,6]


    [3,1,3]
    [3,4,7]

    curr_sum = 0 
    memo = [0] * k
    memo[0] = 1 

    Walk through the arr
        if curr_sum %

    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        memo = {0: 1}
        ans = 0
        for i in nums:
            prefix_sum = (prefix_sum + i)
            if prefix_sum - k in memo:
                ans += memo[prefix_sum-k]
            if prefix_sum in memo:
                memo[prefix_sum] += 1
            else:
                memo[prefix_sum] = 1
        return ans
