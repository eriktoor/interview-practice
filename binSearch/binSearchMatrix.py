class SolutionMatrix2:
    """
https://leetcode.com/problems/search-a-2d-matrix-ii/

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

    """

    def binary_search(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix[0])-1 if vertical else len(matrix)-1

        while hi >= lo:
            mid = (lo + hi)//2
            if vertical: # searching a column
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else: # searching a row
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True
        
        return False

    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        # iterate over matrix diagonals starting in bottom left.
        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True
        
        return False


class SolutionMatrix:
    """

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true


    """


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:  
        if matrix == []: return False 
        
        r, c = len(matrix), len(matrix[0])
                
        left, right = 0, r*c -1
        
        while left <= right: 
            pivot = (left + right) // 2
            
            element = matrix[pivot//c][pivot%c]
            
            if target == element: 
                return True 
            else: 
                if target < element: 
                    right = pivot -1
                else: 
                    left = pivot + 1 
        return False 