"""
Edit Distance: 

Approach 1: Top Down 

Time: O(3 ^ (min(m,n))) where m is the length of word1 and n is the length of word2, Space: O(3 ^ (min(m,n))) calls on the call stack 


Approach 2: Top Down with Memoization 

https://www.geeksforgeeks.org/edit-distance-dp-using-memoization/

Time: O(m x n) where m is the length of word1 and n is the length of word2, Space: O(m x n) + calls on call stack because we only need to keep the last two rows  


Approach 3: Bottom up with Memoization 

Time: O(m x n) where m is the length of word1 and n is the length of word2, Space: O(m) because we only need to keep the last two rows  

Edit Distance: 

0 0 h o r s e 
0 0 1 2 3 4 5 
r 1 1 2 2 3 4
o 2 2 1 2 3 4 
s 3 2 2 2 2 3 


0 0 a b c 
0 0 1 2 3  
a 1 0 1 2 
z 2 1 1 2
c 3 2 2 1


if values are the same, min of diagonal, left and right 
if values are the different, min of diagonal, left and right + 1 
 

"""

class Solution:

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        
        # if one of the strings is empty
        if n * m == 0:
            return n + m
        
        # array to store the convertion history
        d = [ [0] * (m + 1) for _ in range(n + 1)]
        
        # init boundaries
        for i in range(n + 1):
            d[i][0] = i
        for j in range(m + 1):
            d[0][j] = j
        
        # DP compute 
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = d[i - 1][j] + 1
                down = d[i][j - 1] + 1
                left_down = d[i - 1][j - 1] 
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                d[i][j] = min(left, down, left_down)
        
        return d[n][m]

    
    def minDistanceGeeksForGeeks(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # Create a table to store results of subproblems 
        dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 

        # Fill d[][] in bottom up manner 
        for i in range(m + 1): 
            for j in range(n + 1): 

                # If first string is empty, only option is to 
                # insert all characters of second string 
                if i == 0: 
                    dp[i][j] = j    # Min. operations = j 

                # If second string is empty, only option is to 
                # remove all characters of second string 
                elif j == 0: 
                    dp[i][j] = i    # Min. operations = i 

                # If last characters are same, ignore last char 
                # and recur for remaining string 
                elif word1[i-1] == word2[j-1]: 
                    dp[i][j] = dp[i-1][j-1] 

                # If last character are different, consider all 
                # possibilities and find minimum 
                else: 
                    dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                       dp[i-1][j],        # Remove 
                                       dp[i-1][j-1])    # Replace 

        return dp[m][n]    

        
    def minDistanceTopDown(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # If first string is empty, the only option is to 
        # insert all characters of second string into first 
        if m == 0: 
             return n 

        # If second string is empty, the only option is to 
        # remove all characters of first string 
        if n == 0: 
            return m 

        # If last characters of two strings are same, nothing 
        # much to do. Ignore last characters and get count for 
        # remaining strings. 
        if word1[m-1]== word2[n-1]: 
            return self.minDistance(word1[:-1], word2[:-1]) 

        # If last characters are not same, consider all three 
        # operations on last character of first string, recursively 
        # compute minimum cost for all three operations and take 
        # minimum of three values. 
        return 1 + min(self.minDistance(word1, word2[:-1]),    # Insert 
                       self.minDistance(word1[:-1], word2),    # Remove 
                       self.minDistance(word1[:-1], word2[:-1])    # Replace 
                       ) 



class Solutions: 
    def minDistanceTopDown(self, word1: str, word2: str) -> int:
      self.memo = {}
      return self.dp(word1, word2)
      
      
    def dp(self, word1, word2):
        
        if (word1, word2) in self.memo:
          return self.memo[(word1, word2)]
        
        m, n = len(word1), len(word2)
    
        # If first string is empty, the only option is to 
        # insert all characters of second string into first 
        if m == 0: 
             return n 
    
        # If second string is empty, the only option is to 
        # remove all characters of first string 
        if n == 0: 
            return m 
    
        # If last characters of two strings are same, nothing 
        # much to do. Ignore last characters and get count for 
        # remaining strings. 
        if word1[m-1]== word2[n-1]: 
            return self.dp(word1[:-1], word2[:-1]) 
    
        # If last characters are not same, consider all three 
        # operations on last character of first string, recursively 
        # compute minimum cost for all three operations and take 
        # minimum of three values. 
        
        
        # user 
        # user_has_id (id int(10), name varchar(255), )
        # 
        
        #insert = self.minDistance(word1, word2[:-1])
        
        res =  1 + min(self.dp(word1, word2[:-1]),    # Insert 
                       self.dp(word1[:-1], word2),    # Remove 
                       self.dp(word1[:-1], word2[:-1])    # Replace 
                       ) 
        
        self.memo[(word1, word2)] = res
        
        return res 
        
x = Solutions()
x.minDistanceTopDown("geek", "gessek")


                    
                    
        
        
        

