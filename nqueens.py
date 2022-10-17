class Solution:
    """

    Approach: Backtracking 

    Moving left to right, top to bottom 
    1. if a move is valid**, place it 
    2. move to the next row and try to place the next rows queen 
        if this is impossible, return to the previous row and move that queen 
    3. once we have placed n-queens, append that solution to our board 

    [. Q . .]
    [. . . Q]
    [Q . . .]
    [. . Q .]

    State:
    - row 
    - col 

    Base Cases: 
    - row == n (we have placed n queens): return True (append to board)
    - col == n (we couldn't place this queen): return False (backtrack)

    Choices: 
    - place it -> solve(row+1, 0)
    - don't place it continue trying the next col 
    """

    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        board = [["." for i in range(n)] for j in range(n)]

        def is_valid_move(board, r, c):
            directions = [(1, 0), (-1, 0), (0, -1), (0, 1),
                          (1, 1), (-1, -1), (1, -1), (-1, 1)]
            for dr, dc in directions:
                curr_r, curr_c = r+dr, c+dc
                while 0 <= curr_r < n and 0 <= curr_c < n:
                    if board[curr_r][curr_c] == "Q":
                        return False
                    curr_r, curr_c = curr_r + dr, curr_c + dc
            return True

        def solve(r=0, c=0):
            if r == n:
                return True  # we found a solution!
            if c == n:
                return False  # we need to backtrack

            for i in range(n):
                if is_valid_move(board, r, i):
                    board[r][i] = "Q"
                    if solve(r+1, 0):
                        ret.append(copy.deepcopy(board))
                    board[r][i] = "."  # backtrack

        solve()
        # [".","."] --> [".."]
        return [["".join(row) for row in board] for board in ret]
