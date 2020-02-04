"""
===============================================================
Queue's using the queue library

import queue 

queue.get() #gets next element using FIFO
queue.put(val) #adds value to the queue
===============================================================
"""

from queue import Queue

q = Queue()

q.put(4) #add to q 

print("Printing q gives a pointer to the q", q) #prints a pointer to the q 

curr = q.get() #get from q 

print("Current node is ", curr) #prints 4

print("Q-Size is ", q.qsize()) #len(q)


"""
===============================================================
Queue's using the deque library

from collections import dequeu 

queue.popleft() #gets next element using FIFO
queue.append(val) #adds value to the queue
===============================================================
"""

from collections import deque
q = deque() #put and get 
q.append(5)
q.append(4)
print(q)
curr = q.popleft() 
print(q)
print(len(q))

"""
Queue's could also be simulated with 
q = []
q.pop(0), however this would not be constant time pops like using a queue library would
"""


"""
Priority Queues
"""

import heapq 

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 1)
heapq.heappush(heap, 11)

heapq.heappop(heap)

print(heapq.nsmallest(3, heap))