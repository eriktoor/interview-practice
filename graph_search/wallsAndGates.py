"""

Approaches: 

Approach 1: Graph Traversal - BFS 

1. Find all of the cells that are 0 (meaning gates)
    a. store these values in a queue 

Time: O(m x n), Space: O(m x n)

2. while the queue is not empty walk towards every reachable cell 
    a. update value if less than current 
    
Time: O(m x n), Space: O(m x n)


"""


class Solution:

    def wallsAndGatesDFS(self, rooms: List[List[int]]) -> None:
        """
        @desc given an m x n matrix with gates and walls, calculate a cells min distance from a gate in place
        @args  
            @arg1 rooms, an m x n matrix with 0: gate, inf: empty room, -1: a wall 
        @return None, but modify the cells in place
        """
        if not rooms: return 
        
        q = collections.deque()
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.dfs(i,j,0,rooms)

    
    def dfs(self, i, j, count, rooms):
        if i < 0 or j < 0 or i >= len(rooms) or j >= len(rooms[0]) or rooms[i][j] < count: 
            return
        rooms[i][j] = count

        self.dfs(i + 1, j, count + 1, rooms)
        self.dfs(i - 1, j, count + 1, rooms)
        self.dfs(i , j + 1, count + 1, rooms)
        self.dfs(i , j - 1, count + 1, rooms)
    
    
    def bfs(self, q, rooms): 
        
        visited = set()
        while len(q) != 0: 
            curr_i, curr_j, weight = q.popleft()
            visited.add((curr_i,curr_j))

            for new_i, new_j in [(1,0), (0,1), (-1,0), (0,-1)]:
                i = curr_i + new_i
                j = curr_j + new_j
                
                if (i,j) not in visited and i >= 0 and j >= 0 and i <len(rooms) and j < len(rooms[0]) and rooms[i][j] != -1:
                    if weight + 1 < rooms[i][j]:
                        rooms[i][j] = min(weight + 1, rooms[i][j])
                        q.append((i,j,weight + 1))
                    
    
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        @desc given an m x n matrix with gates and walls, calculate a cells min distance from a gate in place
        @args  
            @arg1 rooms, an m x n matrix with 0: gate, inf: empty room, -1: a wall 
        @return None, but modify the cells in place
        """
        if not rooms: return 
        
        q = collections.deque()
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))

        self.bfs(q, rooms)