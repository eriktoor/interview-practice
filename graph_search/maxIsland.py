class Solution:
    """
    https://leetcode.com/problems/max-area-of-island/
    
    """
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        def sinkIsland(grid, i,j): 
            
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0: 
                return 0 
            
            size = 1
            grid[i][j] = 0 
            
            for new_i, new_j in [(1,0), (-1,0), (0,1), (0,-1)]:
                size += sinkIsland(grid, i + new_i, j + new_j)
            
            return size
                
            
            
            
        
        maxSize = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])): 
                if grid[i][j] == 1:
                    curr = sinkIsland(grid,i,j)
                    maxSize = max(curr, maxSize)
                    
        return maxSize 