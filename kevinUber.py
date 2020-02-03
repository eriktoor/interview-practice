class letterCombos: #combination sum
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
