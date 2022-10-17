class Solution:
    """

    Approaches 

    [1 3 4 2]
    [. 2 . .]
    [. . 3 .]
    [. . . 4]


    Choices 
    - place a number 
    - don't place a number

    Base Cases 
    - get past the last row: return true  
    - get to the end of the col: solve(r+1, 0) 
    - 

    State 
    - row
    - col 

    Logic: 
    going from left to right, top to bottom 
        try every value from 1 - 9
            if it is valid ** (TODO what does it mean to be valid)
                place 
                if this solves the board:
                    return 
                backtrack and unplace 

    """

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid_move(r, c, val):
            for i in range(9):
                if board[r][i] == val:
                    return False
                if board[i][c] == val:
                    return False
                if board[3*(r//3) + i // 3][3 * (c//3) + i % 3] == val:
                    return False
            return True

        n = len(board)

        def solve(r=0, c=0):
            if c == n:
                return solve(r+1, 0)
            elif r == n:
                return True
            elif board[r][c] != ".":
                return solve(r, c+1)

            for i in range(1, 10):
                if is_valid_move(r, c, str(i)):
                    board[r][c] = str(i)
                    if solve(r, c + 1):
                        return True
                    board[r][c] = '.'  # BACKTRACK...
            return False

        solve()


"""

    [1 3 2 .]
    [. 2 . .]
    [. . 3 .]
    [. . . 4]

"""


def check_unique(nums):
    s = set()
    for num in nums:
        if num == '.':
            continue

        if num in s:
            return False
        s.add(num)
    return True


def sudoku2(grid):
    for line in grid:
        if not check_unique(line):
            return False

    for i in range(9):
        if not check_unique([line[i] for line in grid]):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not check_unique(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]):
                return False

    return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True
        col_number = {}
        square_number = {}

        for r, row in enumerate(board):
            row_number = []
            for i, number in enumerate(row):
                if number != '.':
                    row_number.append(number)

                    if i in col_number:
                        col_number[i].append(number)
                    else:
                        col_number[i] = [number]

                    index = (r // 3) * 3 + i // 3
                    if index in square_number:
                        square_number[index].append(number)
                    else:
                        square_number[index] = [number]

            if len(row_number) != len(set(row_number)):
                return False

        for col in col_number.values():
            if len(col) != len(set(col)):
                return False

        for square in square_number.values():
            if len(square) != len(set(square)):
                return False

        return valid
