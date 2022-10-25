class Solution:
    
    """

    Approaches 
    
    
    State: 
    - place in word1
    - place in word2 
    
    Choices: 
    - pick both if equal, solve(p1-1,p2-1)
    - delete or insert on word1 solve(p1-1,p2)
    - delete or insert on word2 solve(p1,p2-1)
    
    
    Base Cases: 
    - we get to the end of word2, return len word1
    - we get to the end of word1, return len wod2 

    """
    
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def solve(p1,p2):
            if (p1,p2) in memo: return memo[(p1,p2)]
            if p1 == 0: return p2 
            if p2 == 0: return p1 
            
            pick_it = int(word1[p1-1] != word2[p2-1]) + solve(p1-1,p2-1)
            skip_word1 = 1 + solve(p1-1,p2)
            skip_word2 = 1 + solve(p1,p2-1)
            
            memo[(p1,p2)] = min(pick_it, skip_word1, skip_word2)
            return memo[(p1,p2)]
        
        return solve(len(word1), len(word2))

    def minDistance(self, word1: str, word2: str) -> int:
        """
          # h o r s e 
        # 0 1 2 3 4 5 
        r 1 1 2 2 3 4 
        o 2 2 1 2 3 4 
        s 3 3 2 2 2 3
        
        """
        # Step 1: Init grid with values for # 
        memo = [[i for i in range(len(word1)+1)] for j in range(len(word2)+1)]
        
        for i in range(len(word2)+1):
            memo[i][0] = i 
        
        # Step 2: walk through grid and look at each word 
        for p2 in range(1,len(memo)):
            for p1 in range(1,len(memo[p2])):
                if word1[p1-1] == word2[p2-1]:
                    memo[p2][p1] = memo[p2-1][p1-1]
                else:
                    memo[p2][p1] = 1 + min(memo[p2-1][p1-1], memo[p2-1][p1],memo[p2][p1-1])
        
        return memo[-1][-1]