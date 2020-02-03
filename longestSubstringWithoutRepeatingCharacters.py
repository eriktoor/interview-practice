"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

import unittest
import collections

def sliding_window(string):
  """
  Description: Find the length of the longest substring with unique characters
  
  Input: String
  Output: Integer representing length 
  """
  if len(string) <= 1:
    return len(string)
  
  left, right = 0, 0 
  global_max = float('-inf')
  freq = collections.defaultdict(int)
  
  # Expand Window
  while right < len(string):
    right_char = string[right]
    freq[right_char] += 1
    
    while freq[right_char] == 2:
      global_max = max(global_max, len(string[left:right]))  # TODO: Check this one off 
      left_char = string[left]
      freq[left_char] -= 1
      left += 1
      
    right += 1

  # Process Edge Case
  global_max = max(global_max, len(string[left:right]))  

  return global_max 

"""
     l
    "p w w k e"
     0 1 2 3 4 5
               r 
       
right_char = k
left_char = - 

global_max = 2 

freq = {p:0 ,
        w:1
        k:1
        e:1

        } 

"""

class TestSolution(unittest.TestCase):
  def test_one(self):
    ans = sliding_window('abcabcbb')
    self.assertEqual(ans, 3)
    ans = sliding_window('pwwkew')
    self.assertEqual(ans, 3)
  def test_two(self):
    ans = 1
    self.assertEqual(ans, 1)

    
if __name__ == '__main__':
  unittest.main()
"""
  l
"abcabcbb"
         r
    
global_max = 'abc'

freq = {a:1,
        b:1,
        c:1,}

0. Define a condition to stop expandign the window
  - If the current character count is 2 
  - Check if string[right] == 2 
  
1. Expand the window
1.1 Process the right element 

2. Check if the window meets Step 0. Condition
  2.1 If it does, process the current window
  2.2 Process the left element and contract the window
  
3. Check the edge case 

"""





