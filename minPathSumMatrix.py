class Solution:
    """
    https://leetcode.com/problems/minimum-path-sum/
    
    Input:
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    Output: 7
    Explanation: Because the path 1→3→1→1→1 minimizes the sum.
    
    https://leetcode.com/problems/minimum-path-sum/discuss/360106/Python-Dijkstra-explained-and-commented
    """
    
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
            
            
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
    
    def minPathSum(self, grid): #djikstras
        
        h = [(0, (0,0))] #or alternatively h = [(grid[0][0], (0,0)]
        # build the cost-to-get-to dict:
        cost_to_get_to = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cost_to_get_to[(i,j)] = float('inf')
        cost_to_get_to[(0,0)] = 0 #or alternatively  cost_to_get_to[(0,0)] = grid[0][0]

        visited = set()
        dirs = [(1,0),(0,1)] # left and down
        from heapq import heappop, heappush
        while h:
            cheapestCost, cheapestNode = heappop(h)
            visited.add(cheapestNode)
            x, y = cheapestNode[0], cheapestNode[1]
            for dir in dirs:
                newX, newY = x+dir[0] , y+dir[1]
                # within bounds:
                if newX >= 0 and newX <= len(grid)-1 and newY >= 0 and newY <= len(grid[0])-1:
                    # not seen before:
                    if (newX, newY) not in visited:
                        # check the Djikstra condition
                        edge_cost = grid[newX][newY]
                        if cost_to_get_to[(cheapestNode)] + edge_cost < cost_to_get_to[(newX, newY)]:
                            # update cost and push
                            cost_to_get_to[(newX, newY)] = cost_to_get_to[(cheapestNode)] + edge_cost
                            heappush(h, (cost_to_get_to[(newX, newY)], (newX, newY)))
        return cost_to_get_to[(len(grid)-1,len(grid[0])-1)] + grid[0][0]