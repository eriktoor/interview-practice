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
        
    for i in range(0,9,3):
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

    