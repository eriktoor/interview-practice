"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]



"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or min(candidates) > target: return []
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)



"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

class CombinationSum2:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return  # backtracking 
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]: #avoid recomputation of groups
                continue
            self.dfs(candidates, target-candidates[i], i+1, path+[candidates[i]], res)




"""

State: 
    Index, Nums, Target 

Base Case: 
    Target < 0, return 
    Target == 0, self.ret += 1 

Decisions: 
    Pick Number
    Pick Number and Pick it Again 
    Skip Number 

https://leetcode.com/problems/combination-sum-iv/submissions/
"""

class combinationSum4:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        self.table = {}
        return self.helper(target, nums, 0)

    def helper(self, target, nums, idx):
        if idx == len(nums): return 0
        if target in self.table:
            return self.table[target]
        if target < 0:
            return 0
        elif target == 0:
            return 1
        count = 0
        
#         pick_number = self.helper(target - nums[idx], nums, idx)
#         # pick_again = self.helper(target - nums[idx], nums, idx)
#         skip_number = self.helper(target, nums, idx + 1)
        
#         count = pick_number + skip_number
#         return count 
               
        for idx, n in enumerate(nums):
            count += self.helper(target - n, nums, idx)
        self.table[target] = count
        return count















class TargetSum:
    # https://leetcode.com/problems/target-sum/solution/

    """

    Approaches:  


    Approach 1: DP 

    Input: nums is [1, 1, 1, 1, 1], S is 3. 
    Output: 5

    [1, 1, 1, 1, 1]
    ^ 

    State: 
        - which index i'm on **
        - nums 
        - target 
    Base Case: 
        - if taget == 0 and i haven't used this before
            increment numWays
        - otherwise 
            backtrack 
        - idx is at end and target != 0 
        - we have the solution stored in memo 
    Decisions: 
        - add the value at the current index
        - subtract the value at the current index
        
        add_number = helper(nums, idx, memo, target)
        subtract_number = helper(nums, idx, memo, target)
        


    [1,1,1,1,1], 3
    
    
    

    Pseudocode 
    
    def helper(nums, idx, memo, target): 
        if (idx, target) in memo: 
            return memo[(idx, target)]
        if target == 0 and (idx, target) not in memo: 
            memo[(idx, target)] = 1
            return memo[(idx, target)]
        if idx == len(nums) and target != 0: 
            memo[(idx, target)] = 0 
            return memo[(idx, target)]
            
        add_number = helper(nums , idx+1, memo, target+ nums[idx])
        subtract_number = helper(nums , idx+1, memo, target-nums[idx])
        memo[(idx, target)] = add_number + subtract_number
        return memo[(idx, target)]

    helper(nums, 0, memo, S, 0)
    
    
    
    """


    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        return self.dp(nums, S, 0, 0)
        
    def dp(self, nums, S, remain, index):
        if S == remain and index == len(nums):
            return 1
        elif index == len(nums):
            return 0
        
        positive = self.dp(nums, S, remain + (nums[index]), index+1)
        negative = self.dp(nums, S, remain + (-nums[index]), index+1)

        return positive + negative

class Solution:
    # https://leetcode.com/problems/target-sum/solution/
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        return self.dp(nums, S, 0, 0, {})
        
    def dp(self, nums, S, remain, index, memo):
        if (remain, index) in memo:
            return memo[(remain, index)]
        if S == remain and index == len(nums):
            return 1
        elif index == len(nums):
            return 0
        
        positive = self.dp(nums, S, remain + (nums[index]), index+1, memo)
        negative = self.dp(nums, S, remain + (-nums[index]), index+1, memo)
        memo[(remain, index)] = positive + negative
        return memo[(remain, index)]