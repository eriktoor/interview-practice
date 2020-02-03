def array_of_array_products_faster(nums):
        length = len(nums)
        answer = [0 for i in range(length)]
    
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
      
        R = 1;
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer

def array_of_array_products(arr):
  """
  @desc will place the product of all vals in the array except the val at that index at each index
  @args arr which will be a list
  @return ret which will be a list
 
  @example invoation
  >>>array_of_array_products([1,2])
  [2,1]
  >>>array_of_array_products([1])
  []
  >>>array_of_array_products([1,2,3])
  [6,3,2]
  """
  if len(arr) <= 1: return []
 
  ret = [1 for i in range(len(arr))]
 
  count = 0
 
  while count < len(arr):
    for i in range(len(arr)):
      if i != count:
        ret[count] *= arr[i]
    count += 1  
 
  return ret


arr = [8, 10, 2]
"""
desired out --> [20, 16, 80]
ret = [20,16,80]

"""

print(array_of_array_products(arr))