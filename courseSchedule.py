


class SolutionCourseSchedule:
    """
    https://leetcode.com/problems/course-schedule/


    Topological Sort: https://leetcode.com/problems/course-schedule/discuss/58537/AC-Python-topological-sort-52-ms-solution-O(V-%2B-E)-time-and-O(V-%2B-E)-space

    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:   
        graph, visited = {}, {}
        
        for i in range(numCourses):
            visited[i] = 0
            graph[i] = set()
        for p in prerequisites:
            graph[p[1]].add(p[0])
            
        for key in graph: 
            if self.dfs(key, graph, visited) == False: return False 
        
        return True 


    def dfs(self, curr, graph, visited):
        if visited[curr] == 1: return True #don't do a dfs again
        if visited[curr] == -1: return False #theres a cycle, curr is a back edge 
        visited[curr] = -1
        for child in graph[curr]:
            if not self.dfs(child, graph, visited):
                return False
        visited[curr] = 1
        return True
        
        

class SolutionCourseSchedule2:
    """
    https://leetcode.com/problems/course-schedule-ii/
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, visited = {}, {}
        
        for i in range(numCourses): 
            visited[i] = 0 
            graph[i] = set() 
            
        for p in prerequisites: 
            graph[p[1]].add(p[0])
            
        res = []
        
        for key in graph:
            if self.dfs(key, res, graph, visited) == False: return []
        
        return res 
    
    def dfs(self, curr, result, graph, visited):
        if visited[curr] == 1: return True
        elif visited[curr] == -1: return False
        visited[curr] = -1
        
        for child in graph[curr]:
            if self.dfs(child, result, graph, visited) == False: return False
            
        visited[curr] = 1
        result.insert(0, curr)
        return True

        