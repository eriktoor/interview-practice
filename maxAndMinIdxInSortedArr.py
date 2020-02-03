"""

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/

Approaches:

Approach 1: Binary Search 

Taking advantage of the array being sorted we can conduct a binary search on the array with an extra left and right check 

binary search is log_n time 


      m
1, 3, 3, 6, 6, 7
      L  
         R
"""

        
class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    # [1,2,3,3,4,4,4]
    def extreme_insertion_index(self, nums, target, left):
        left_idx = 0
        right_idx = len(nums)

        while left_idx < right_idx:
            pivot = left_idx + (right_idx - left_idx) // 2
            if nums[pivot] > target or (left and target == nums[pivot]):
                right_idx = pivot #because of this case, we need to return function - 1
            else:
                left_idx = pivot+1

        return left_idx

    def searchRange1(self, nums, target):
        """
        @desc find the first and last index of a target value in a sorted arr
        @args
            @arg1 nums a list of integers that is sorted
            @arg2 target an int that is the value we are looking for in our sorted arr
        @return an array with the [first, last] index the values are located at
        """
        
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]

    def searchRange(self, nums, target):
        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                pivot = left + (right-left) // 2
                if x > A[pivot]: left = pivot + 1
                else: right = pivot - 1
            return left

        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                pivot = left + (right- left) // 2
                if x >= A[pivot]: left = pivot + 1
                else: right = pivot - 1
            return right

        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]
    
    


    
            