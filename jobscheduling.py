
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/submissions/
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
                
        intervals = [[start,end,profit] for start,end,profit in zip(startTime, endTime, profit)]
        intervals.sort() 
        memo = {}
        
        def solve(i):
            if i in memo: return memo[i]
            if i == len(startTime): return 0
            
            j = i + 1 
            while j < len(startTime) and intervals[i][1] > intervals[j][0]:
                j+= 1 
            
            pick_it = intervals[i][2] + solve(j)
            skip_it = solve(i+1)
            memo[i] = max(pick_it, skip_it)

            return memo[i]
        
        
        return solve(0)