"""
Approach 1: Top-Down 

Base Case: If we are on the first row or the first column then there is one way to get there
Recursive call the function for uniquePaths(m-1,n) and uniquePaths(m, n-1)

Time: O(m x n), Space: O(m x n) calls to the call stack 

Approach 2: Bottom-Up

Matrix representing grid that we store subproblems initialized to one bc the first row and column only have 1 way to go  
We always store the left + top rows value in 

[1,1,1]
[1,2,3]

https://leetcode.com/problems/unique-paths/

"""


class Solution:
    
    def __init__(self):
        pass
    
    def uniquePathsTopDown(self, m, n):
        
        if(m == 1 or n == 1): #if we're on the first row or column we only have one way to get there 
            return 1
  
        # If diagonal movements are allowed 
        # then the last addition 
        # is required. 
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1) 
        
    def uniquePaths(self, m, n):
        """
        @desc find the number of possible baths from the top left to the bottom right
        @args 
            @arg1 m which is an integer representing how many columns there will be
            @arg2 n which is an integer representing how many rows there will be
        @return some integer, paths which is the number of paths that exist 
        """
        
        if m == 0 or n == 0: return 1 
        
        numPaths = 0 
        
        dp = [[1 for i in range(m)] for j in range(n) ]
        
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        numPaths = dp[-1][-1]
        
        return numPaths 
    

    






'''
reach n-1, n - 1

Ex) 4 

grid 4 x 4 , dest is (3,3)

 counter [(i, j)] = counter[(i, j+1)] + counter[(i+1, j)]

possibilities: E, N 

East Movement) i, j ==> i, j + 1
North Movement) i, j ==> i+1, j 

def num_of_paths_to_dest(n):
  counter = 0 

  i, j = n -1, 0

  counter = helper(i, j +1, n, counter + 1)
  
  return counter
    

helper(i, j, path, n, counter):
  options = [(0, 1), (1, 0)]

  final_dest = (n-1, n-1)
  if (i,j) == final_dest:
    return counter
  
  for path in options:
    if i == final_dest[0] and path[0] == 1:
      pass
    elif j == final_dest[1] and path[1] == 1:
      pass
    else:
      helper(i + path[0], j + path[1], n, counter + 1)
  
  
    

'''

def num_of_paths_to_dest(n):
  counter = 0 

  i, j = 0 , 0
  
  if n == 1: return 1
  
  mem = [[-1 for x in range(n)] for y in range(n)]

  counter = helper(i + 1, j, n, mem)
  
  return counter


def helper(i, j, n, mem):
  if mem[i][j]>-1:
    print("HERE")
    return mem[i][j]
  options = [(0, 1), (1, 0)]

  final_dest = (n-1, n-1)
  if i==(n-1) and j==(n-1):
    return 1
  
  counter = 0
  for path in options:
    if i == n - 1 and path[0] == 1:
      pass
    elif j == i and path[1] == 1:
      pass
    else:
      counter += helper(i + path[0], j + path[1], n, mem)
  mem[i][j] = counter
  print(mem)
  return counter

print(num_of_paths_to_dest(1))  
  
'''
[
  [-,-,-,5]
  [-,-,2,5]
  [-,1,2,3]
  [1,1,1,1]  
]  
https://www.pramp.com/challenge/N5LYMbYzyOtbpovQoY7X

0 0 0 5
0 0 2 5
0 1 2 3
1 1 1 1


'''





#THIS DOE NOT WORK 


def numPathsBottomUp(n):
  dp = [[0]*n for _ in range(n)]

  dp[n-1][0] = 1
  for i in range(n-1,-1,-1):
    for j in range(i, ):
      if i == n - 1 and j == 0: 
        continue
      dp[i][j] = getPrevValues(i,j,dp)
    
  return dp[0][n-1]

def getPrevValues(i,j,dp):
  if j > 0: 
    return 0 
  v1, v2 = 0,0

  if j - 1 >= 0 and i >= j - 1:
    v1 = dp[i][j-1]
  if i - 1 >= 0 and i - 1 >= j: 
    v2 = dp[i-1][j]
  
  return v1 + v2 


print(numPathsBottomUp(4))