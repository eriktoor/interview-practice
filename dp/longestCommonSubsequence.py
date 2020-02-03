"""
Longest Common Subsequence

0 0 d o g 
0 0 0 0 0 
f 0 0 0 0 
r 0 0 0 0 
o 0 0 1 1 
g 0 0 1 2 

Bottom Up: 

If they are the same take the max of the left right and above and add 1
if they are different take the max of the left right and above

"""



"""
Longest Common Subsequence 


Approach 1: Top Down 

Termination Condition is you reach the end of one string 

Else you would either recurse on 1 + the function if they are equal 
and or recurse on the max(stepping forward in word1 in fct, stepping forward in word2 in fct)

Time: O(2^n) , Space: O(2^n) calls on the call stack 


Approach 2: Top Down with Memoization 

Time: O(m x n), Space: O(m x n) for the memo matrix plus the calls to call stack

Approach 3: Bottom up with memoization 

Time: O(m x n) and Space: O(m x n)

https://leetcode.com/problems/longest-common-subsequence/discuss/436719/Python-very-detailed-solution-with-explanation-and-walkthrough-step-by-step.

0 a b c d e
a 1 0 0 0 0
c 0 0 1 0 0
e 0 0 0 0 1


0 0 a b c d e
0 0 0 0 0 0 0
a 0 1 1 1 1 1
c 0 1 1 2 2 2
e 0 1 1 2 2 3


case 1: 
s1[i] == s2[j]: 
  recurse on 1 +  s2[j-1], s1[i-1]
  
s1[i] != s2[j]:
  recurse on max( LCS(s2[j-1], s1[i]), LCS(s2[j], s1[i-1])


"""


class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if s1[row - 1] == s2[col - 1]:
                    memo[row][col] = 1 + memo[row - 1][col - 1]
                else:
                    memo[row][col] = max(memo[row][col - 1], memo[row - 1][col])

        return memo[m][n]

    def longestCommonSubsequenceTopDownDP(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return self.helperTopDownDP(s1, s2, 0, 0, memo)

    def helperTopDownDP(self, s1, s2, i, j, memo):
        if memo[i][j] < 0:
            if i == len(s1) or j == len(s2):
                memo[i][j] = 0
            elif s1[i] == s2[j]:
                memo[i][j] = 1 + self.helperTopDownDP(s1, s2, i + 1, j + 1, memo)
            else:
                memo[i][j] = max(
                    self.helperTopDownDP(s1, s2, i + 1, j, memo),
                    self.helperTopDownDP(s1, s2, i, j + 1, memo),
                )
        return memo[i][j]
        
    def longestCommonSubsequenceTopDown(self, s1: str, s2: str) -> int:
        return self.helperTopDown(s1, s2, 0, 0)

    def helperTopDown(self, s1, s2, i, j):
        if i == len(s1) or j == len(s2):
            return 0
        if s1[i] == s2[j]:
            return 1 + self.helperTopDown(s1, s2, i + 1, j + 1)
        else:
            return max(self.helperTopDown(s1, s2, i+1, j), self.helperTopDown(s1, s2, i, j + 1))

                    