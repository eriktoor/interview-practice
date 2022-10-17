"""
https://leetcode.com/problems/permutations/discuss/993970/Python-4-Approaches-%3A-Visuals-%2B-Time-Complexity-Analysis
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        n = len(nums)

        def permute(ptr):
            if ptr == n:
                ret.append(nums[:])

            for i in range(ptr, n):
                nums[i], nums[ptr] = nums[ptr], nums[i]
                permute(ptr+1)
                nums[i], nums[ptr] = nums[ptr], nums[i]

        permute(0)
        return ret


"""

recursive with implicit stack 
def recursive(nums, perm=[], res=[]):
        
            if not nums: 
                res.append(perm) # --- no need to copy as we are not popping/backtracking. Instead we're passing a new variable each time 

            for i in range(len(nums)): 
                newNums = nums[:i] + nums[i+1:]
                # perm.append(nums[i]) # --- instead of appending to the same variable
                newPerm = perm + [nums[i]] # --- new copy of the data/variable
                recursive(newNums, newPerm, res) 
                # perm.pop()  # --- no need to backtrack
            return res
        
        return recursive(nums)


"""


"""
DFS with explicit stack
def recursive(nums):
	 stack = [(nums, [])]   # -- nums, path (or perms)
	 res = []
	 while stack:
		 nums, path = stack.pop()
		 if not nums:
			 res.append(path)
		 for i in range(len(nums)):   # -- NOTE [4]
			 newNums = nums[:i] + nums[i+1:]
			 stack.append((newNums, path+[nums[i]]))  # --  just like we used to do (path + [node.val]) in tree traversal
	 return res

# NOTE [4]
# The difference between itertaive tree/graph traversal we did before and this one is that
# in most tree/graph traversals we are given the DS (tree/graph/edges) whereas here we have to build the nodes before we # traverse them
# Generating the nodes is very simple, we Each node will be (nums, pathSofar)

"""

"""
BFS with iterative queue

def recursive(nums):
	from collections import deque
	q = deque()
	q.append((nums, []))  # -- nums, path (or perms)
	res = []
	while q:
		nums, path = q.popleft()
		if not nums:
			res.append(path)
		for i in range(len(nums)):
			newNums = nums[:i] + nums[i+1:]
			q.append((newNums, path+[nums[i]]))
	return res
"""
