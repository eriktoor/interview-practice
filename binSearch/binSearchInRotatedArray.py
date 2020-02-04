
class Solution:
    def search(self, arr, target):
        ret = -1 


        left, right = 0 , len(arr) - 1


        while left <= right: 
            pivot = left + (right - left) // 2

            if arr[pivot] < arr[left]: 
                left_sorted = False
            else:
                left_sorted = True 

            if arr[pivot] == target:
                return pivot

            val = target
            if left_sorted:
                if arr[left] <= val < arr[pivot]: 
                    right = pivot - 1 
                else:
                    left = pivot + 1 
            else:
                if arr[pivot] < val <= arr[right] and not left_sorted: 
                    left = pivot + 1 
                else:
                    right = pivot - 1 

        return ret
 


"""
https://www.youtube.com/watch?v=GU7DpgHINWQ

Approach: Binary Search



[1,2,3,4,5,9]
 l 
           r
           
Base Case: No rotation

[6,7,1,2,3,4]
 l
           r
     m

if m < l: right side is sorted 


[6,7,9,10,2,3,4]
 l
              r
        m

if m > l: left side is sorted 



Pseudocode: 

left, right ptrs 
pivot = left + (right - left) // 2

while left <= right: 
  
  #establish sorted side 
  
  if val is between left and val is between middle and left: 
    decrement right 
  elif val is not between between left and middle and left:
    increment left 
    
  elif val is between middle and right and right: 
    increment left
  elif val is not between middle and right and right:
    decrement right 
  else: 
    return index 
    
 return left 


               


"""

def binSearchInRotatedArray(arr, target): 
  """
  @desc find index of target value in rotated sorted array 
  @args
    @arg1 arr which is an array which was sorted but then shifted some k indices
    @arg2 target value
  @return ret the index of a target value 
  """
  ret = -1 
  
  
  left, right = 0 , len(arr) - 1
  

  while left <= right: 
    pivot = left + (right - left) // 2

    if arr[pivot] < arr[left]: 
      left_sorted = False
    else:
      left_sorted = True 
      
    if arr[pivot] == target:
      return pivot
    
    val = target
    if left_sorted:
      if arr[left] <= val < arr[pivot]: 
        right = pivot - 1 
      else:
        left = pivot + 1 
    else:
      if arr[pivot] < val <= arr[right] and not left_sorted: 
        left = pivot + 1 
      elif val > arr[pivot] and not left_sorted:
        right = pivot - 1 
  return ret


arr = [6,7,1,2,3,4]
target = 4

"""
[6,7,1,2,3,4]



right = 2

left = False, sorted Right


"""

print(binSearchInRotatedArray(arr, target)) #0
  
  
