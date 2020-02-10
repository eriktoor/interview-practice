class letterCombos: #combination sum
    # https://leetcode.com/problems/letter-combinations-of-a-phone-number/
    def letterCombinations(self, digits: str) -> List[str]:
        
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            if len(next_digits) == 0: # 0 digits to check
                output.append(combination)
                
            else:  # if there are still digits to check
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
                    
                    
        output = []
        if digits:
            backtrack("", digits)
        return output



"""https://leetcode.com/problems/task-scheduler/discuss/130786/Python-solution-with-detailed-explanation"""
class TaskScheduler:
    """
    greedy algo
    
    Exampe: Say we have the following tasks: [A,A,A,B,C,D,E] with n =2
    Now if we schedule using the idea of scheduling all unique tasks once and then calculating if a cool-off is required or not, then we have: A,B,C,D,E,A,idle,dile,A i.e. 2 idle slots.
    But if we schedule using most frequent first, then we have:
    2.1: A,idle,idle,A,idle,idle,A
    2.2: A,B,C,A,D,E,A i.e. no idle slots. This is the general intuition of this problem.
    3.The idea in two can be implemented using a heap and temp list. This is illustrated in the code below.
    4.Time complexity is O(N * n) where N is the number of tasks and n is the cool-off period.
    5.Space complexity is O(1) - will not be more than O(26).
    
    
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        from heapq import heappush, heappop, heapify
        curr_time, h = 0, []
        for k,v in Counter(tasks).items():
            heappush(h, (-1*v, k))
        while h:
            i, temp = 0, []
            while i <= n:
                curr_time += 1
                if h:
                    x,y = heappop(h)
                    if x != -1:
                        temp.append((x+1,y))
                if not h and not temp:
                    break
                else:
                    i += 1
            for item in temp:
                heappush(h, item)
        return curr_time


class minMeetingRooms:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        Time: O(n), constructing min heap w n elments 
        Space: O(n)
        """
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]: #0 is start, 1 is end 
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class MergeKLists:
    def mergeKLists(self, lists): 
        import heapq
        
        heap = []
        
        for head in lists: 
            while head != None:
                heapq.heappush(heap, head.val)
                head = head.next
        
        print(heap)
        dummy = ListNode(-1)
        head = dummy
        
        while len(heap) != 0: 
            head.next = ListNode(heapq.heappop(heap))
            head = head.next
            
        return dummy.next
                    
    
    def mergeKListsMergeSort(self, lists: List[ListNode]) -> ListNode:     
        
        if len(lists) == 0: return 
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TextJustification:
    """
    
    https://leetcode.com/problems/text-justification/submissions/
    """
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        length_list = list(map(len,words))        
        idx = 0
        ret = []
        while(idx < len(words)):
            s = idx
            while(idx < len(words) and (sum(length_list[s:idx+1])+idx-s) <= maxWidth):
                idx += 1
            
            tmp = words[s]
            if idx-s ==1:               # if there is only one word
                tmp += ' '* (maxWidth-len(tmp))
            elif idx == len(words):     # if this is the last element
                tmp = ' '.join(words[s:idx])
                tmp += ' '* (maxWidth-len(tmp))
            else:         # normal case
                minLength = (idx-s-1) + sum(length_list[s:idx])     # minimum length is number of space + total length of strings
                numExSpace = maxWidth - minLength
                unitSpace = numExSpace//(idx-s-1)
                extraSpace = numExSpace % (idx-s-1)
                tmp = words[s]
                for i in range(s+1, idx):
                    # add space
                    extra = 1 if i-s <= extraSpace else 0
                    space = ' '*(1+unitSpace+extra)
                    tmp += space
                    # add next word
                    tmp += words[i]
            
            
            ret.append(tmp)
        return ret



'''
The logs are already sorted by timestamp.
Use a stack to store tasks. Only the task on stack top got executed.
When a new task comes in, calculate the exclusive time for the previous stack top task.
When a task ends, remove it from stack top.
Because of single thread, task on stack top is guaranteed to ends before other tasks.
Record the time of previous event to calcualte the time period.
Time: O(n)
Space: O(n)
https://leetcode.com/problems/exclusive-time-of-functions/submissions/
'''
class ExclusiveTime:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        if not n or not logs:
            return 0
        task_stack = []
        res = [0]*n
        pre_event = 0
        for log in logs:
            data = log.split(':')
            if data[1] == 'start':
                if not task_stack:
                    task_stack.append(int(data[0]))
                    pre_event = int(data[2])
                else:
                    pre_task = task_stack[-1]
                    res[pre_task] += int(data[2]) - pre_event
                    task_stack.append(int(data[0]))
                    pre_event = int(data[2])
            else:
                pre_task = task_stack.pop()
                res[pre_task] += int(data[2]) - pre_event + 1
                pre_event = int(data[2]) + 1
        return res


class Solution:
    """
    https://leetcode.com/problems/critical-connections-in-a-network/submissions/
    
    """
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        graph = [[] for _ in range(n)] ## vertex i ==> [its neighbors]
		
        currentRank = 0 ## please note this rank is NOT the num (name) of the vertex itself, it is the order of your DFS level
		
        lowestRank = [i for i in range(n)] ## here lowestRank[i] represents the lowest order of vertex that can reach this vertex i
		
        visited = [False for _ in range(n)] ## common DFS/BFS method to mark whether this node is seen before
        
        ## build graph:
        for connection in connections:
            ## this step is straightforward, build graph as you would normally do
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
        
        res = []
        prevVertex = -1 ## This -1 a dummy. Does not really matter in the beginning. 
		## It will be used in the following DFS because we need to know where the current DFS level comes from. 
		## You do not need to setup this parameter, I setup here ONLY because it is more clear to see what are passed on in the DFS method.
		
        currentVertex = 0 ## we start the DFS from vertex num 0 (its rank is also 0 of course)
        self._dfs(res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex)
        return res
    
    def _dfs(self, res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex):

        visited[currentVertex] = True # it is possible 
        lowestRank[currentVertex] = currentRank

        for nextVertex in graph[currentVertex]:
            if nextVertex == prevVertex:
                continue ## do not include the the incoming path to this vertex since this is the possible ONLY bridge (critical connection) that every vertex needs.

            if not visited[nextVertex]:
                self._dfs(res, graph, lowestRank, visited, currentRank + 1, currentVertex, nextVertex)
				# We avoid visiting visited nodes here instead of doing it at the beginning of DFS - 
				# the reason is, even that nextVertex may be visited before, we still need to update my lowestRank using the visited vertex's information.

            lowestRank[currentVertex] = min(lowestRank[currentVertex], lowestRank[nextVertex]) 
			# take the min of the current vertex's and next vertex's ranking
            if lowestRank[nextVertex] >= currentRank + 1: ####### if all the neighbors lowest rank is higher than mine + 1, then it means I am one connecting critical connection ###
                res.append([currentVertex, nextVertex])



"""
https://leetcode.com/problems/construct-quad-tree/submissions/
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class ConstructQuadTree:
    def construct(self, grid: List[List[int]]) -> 'Node':
        """
        @desc 
        
        """
    def construct(self, grid):
        return grid and self.dfs(0, 0, len(grid), grid) if grid else None
    def dfs(self, i, j, l, grid):
        if l == 1:
            node = Node(grid[i][j] == 1, True, None, None, None, None)
        else:
            tLeft = self.dfs(i, j, l // 2, grid)
            tRight = self.dfs(i, j + l // 2, l // 2, grid)
            bLeft = self.dfs(i + l // 2, j, l// 2, grid)
            bRight = self.dfs(i + l // 2, j + l // 2, l // 2, grid)
            value = tLeft.val or tRight.val or bLeft.val or bRight.val
            if tLeft.isLeaf and tRight.isLeaf and bLeft.isLeaf and bRight.isLeaf and tLeft.val == tRight.val == bLeft.val == bRight.val:
                node = Node(value, True, None, None, None, None)
            else:
                node = Node(value, False, tLeft, tRight, bLeft, bRight)
        return node
    
    
