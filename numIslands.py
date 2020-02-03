
"""
Approaches:

Pseudocode: numIslands
for each row in the matrix
    for each col in the row 
        if matrix at row and column is 1 call dfs or bfs
        increment numIslands
return numIslands

Time: O(m x n), Space: O(1)

Approach 1: DFS
mark current cell at row, col as visited
    recurse on top bottom right left until all cells are visited

Time: O(m x n), Space: O(m x n) calls to call stack

Approach 2: BFS
mark current cell at row as visited 
    initialize queue 
    while queue isnt empty
        visit those values
            add values that are 1 to queue to visit

Time: O(m x n), Space: O(m x n) values in queue

Total Time: O(m x n), Total Space: O(m x n) 

"""

def numIslands(binaryMatrix):
    """
    @desc find the num of Islands where islands are a block of 1's
    @args
        @arg1 binaryMatrix which is an list of lists with 1's and 0's
    @return numIslands int showing the groupings of 1s
    """
    numIslands = 0 
    for i in range(len(binaryMatrix)): #for each row
        for j in range(len(binaryMatrix)): #for each column
            if binaryMatrix[i][j] == 1:
                dfs(binaryMatrix, i , j)
                numIslands += 1 
    return numIslands 

def dfs(binaryMatrix, i, j):
    
    binaryMatrix[i][j] = "0"

    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    for new_i, new_j in directions: 
        new_i += i
        new_j += j
        if new_i >=0 and new_j >= 0 and new_i < len(binaryMatrix) and new_j < len(binaryMatrix[0]) and binaryMatrix[new_i][new_j] == 1:
            dfs(binaryMatrix, new_i, new_j)



binaryMatrix = [ [0,    1,    0,    1,    0],
                [0,    0,    1,    1,    1],
                [1,    0,    0,    1,    0],
                [0,    1,    1,    0,    0],
                [1,    0,    1,    0,    1] ]

print(numIslands(binaryMatrix))