class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        """
        @desc find if adjacent letters can be connected on a matrix to make a word
        @args
            @arg1 board, an m x n matrix that has characters as each value
            @arg2 word, a string that we are trying to see if we can create from chars in board
        @ret boolean if word can be found in board 
        
        
        Graph Traversal - DFS 
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]

        "ABCCED"
        """
        
        if not word or not board: return False 
                           
        
        def dfs(i, j, count, board, word): 
            if count == len(word): return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[count]:
                return False

            temp = board[i][j]
            board[i][j] = " "
            found = dfs(i+1, j, count+1, board, word) or dfs(i-1, j, count+1, board, word) or dfs(i, j+1, count+1, board, word) or dfs(i, j-1, count+1, board, word)
            board[i][j] = temp

            return found 
                
        
        for i in range(len(board)): 
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i,j,0,board,word):
                    return True
            
        return False 
    
    
    
    
    
    
    
    
    def existBT(self, board: List[List[str]], word: str) -> bool:
        if not word or not board or not board[0]:
            return False
        m,n = len(board), len(board[0])
        starts=[]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    starts.append([i,j])
        
        def backtrack (i,j,p):
            if p == len(word):
                return True 
            res = False
            for ni, nj, in [(i-1,j), (i+1,j), (i,j-1), (i, j+1)]:
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == word[p]:
                    tmp = board[ni][nj]
                    board[ni][nj] = "#"
                    if backtrack(ni, nj, p+1):
                        res = True
                        break
                    board[ni][nj] = tmp
            return res

        for i, j in starts:
            tmp = board[i][j]
            board[i][j] = '#'
            if backtrack(i, j, 1):
                return True
            board[i][j] = tmp
        
        
        
        
        