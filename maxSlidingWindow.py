class Solution:

    """

    Approaches: 

    Approach 1: checking the max in every window 

    For the window size
    - move from 0 to n - k + 1 

    O(k * (N- K)) time 
    O(1) space


    Approach 2: using a monotonic decreasing queue 

    for the window 
    while not at the end 
        for every value at the end of the queue less than the curr right val   
            pop it off the queue bc we ll never need it 
        then add the item to the end of the queue 

    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        @desc for each window size k moving from left --> right, append the max of that window
        @args
            @arg1 nums a list of nums
            @arg2 k an int representing a window 
        @return ret a list holding the max val from each window
        """
        ret = []
        l, r = 0, 0
        n = len(nums) - 1
        from collections import deque
        deq = deque()  # Note: we will maintain this as a decreasing monotonic queue

        while r <= n:
            while deq and nums[r] > deq[-1]:
                deq.pop()
            deq.append(nums[r])

            if k - 1 == r - l:
                ret.append(deq[0])
                # print(k, r, l, deq)
                if deq[0] == nums[l]:
                    deq.popleft()
                l += 1

            r += 1

        return ret


"""
nums = [1,3,-1,-3,5,3,6,7]
        l
             r
k = 3
ret = [3,]
q = [3, -1]
l = 1 
r = 2 

"""
