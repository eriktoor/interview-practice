#jaesain@amazon.com
#Julian Esain

#https://leetcode.com/problems/shortest-path-in-binary-matrix/
#https://leetcode.com/problems/network-delay-time/

"""

Modularized Weights

Approaches: 

Approach: Djikstras -- Weights

1. Build directed graph based upon times array 

graph = {} # key: {(node, weight),()}
weights = {} @ key: float(inf)

#u, v, w = times[0] #u is source, v is target, w is weight between 
iterate over times and unpack times subarrays: 
  graph[u].add((v, w))


2. Conduct Djikstras on all nodes in the graph 

BFS with a minheap

add adjacent nodes to minheap
create visited set 

while heap: 
  pop minweight node 
    add its adjacent nodes if not visited 
    update min weights to see if less than current 


3. return the maximum of all of the minimum times
iterate over weights 
  find max


"""


def networkDelayTime(times, N, K): 
  """
  @desc given a list of times find how long it will take for all nodes to receive a message
  @args
    @arg1 a list of the times it takes for a message to get from the source to a target node 
    @arg2 N, an int representing the number of nodes
    @arg3 K, an int representing the starting node 
  @return min time it takes for all nodes to receive the message
  """
  
  minTime = -1 
  
  #Step 1: Create a Direct Graph 
  
  graph = {} # where key is a Node source and value is Node, weight with v,weight
  weights = {} # each node mapped to its min weight Node 
  # [2,1,1], [2,3,1]
   
  for u, v, w in times: 
    if u not in weights: 
      weights[u] = float("inf")
    if v not in weights:
      weights[v] = float("inf")
    
    if u not in graph: 
      graph[u] = set()
    if v not in graph:
      graph[v] = set()
    graph[u].add((w, v))
  #Step 2: Run djikstras on the Directed Graph 
  weights[K] = 0
  
  visited = set() 
  
  from heapq import heappop, heappush
  
  heap = [] #initialized array that will be heap 
  
  for w, n in graph[K]:
    heappush(heap, (w,n))
    
  visited.add(K)

  
  while len(heap) > 0: 
    currWeight, currNode = heappop(heap) #pop the minweight node 
    weights[currNode] = currWeight
    if currNode not in visited: # add its adjacent nodes if not visited
      #print(currNode, currWeight)
      for w, n in graph[currNode]: #Add its items 
        #UPDATE MIN WEIGHT 
        weights[n] = currWeight
        heappush(heap, (w + currWeight, n)) #TODO: should be w + currWeight?
      visited.add(currNode)
  
  #Step 3: Iterate over weights
  maxWeight = float("-inf")
  for n, w in weights.items():
    maxWeight = max(maxWeight, w)
  
  
#  return max(maxWeight.values()) if max(maxWeight.values()) != float('inf') else -1 
  
  
  return minTime if maxWeight == float("inf") else maxWeight 

  """
  Input: times = [[2,1,1],[2,3,1],[3,4,1]]
  N = 4
  K = 1

  1, 1

  heap = [(1,4)]

  graph = {
    2 : {(1,1), (1,3)}
    1 : 
    3 : {(1, 4)}
    4 : 
  }
  weight = {
    2 : 0
    1 : 1
    3 : 1
    4 : 2
  }

  """


import unittest

class Test(unittest.TestCase): 
  def test_valid(self):
    """
    Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 1
    
    """
    
    times = [[2,1,1],[2,3,1],[3,4,1]]
    N = 4
    K = 2
    ans = networkDelayTime(times, N, K)
    self.assertEquals(ans, 2) 
    times = [[2,1,1],[2,3,1],[10,4,1]]
    N = 4
    K = 1
    ans = networkDelayTime(times, N, K)
    self.assertEquals(ans, -1)
    

# if __name__ == '__main__':
#  unittest.main()

times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
print(networkDelayTime(times, N, K))


times = [[2,1,1],[10,3,1],[3,4,1]]
N = 4
K = 2
print(networkDelayTime(times, N, K))