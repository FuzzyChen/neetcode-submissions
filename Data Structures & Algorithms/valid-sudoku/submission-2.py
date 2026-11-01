class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # make 3 set 
        col = [set() for _ in range(9)]
        row = [set() for _ in range(9)]
        box = [set() for _ in range(9)]


        for r in range(9):
            for c in range(9):
                #condition which boxx it is 
                if board[r][c] == ".":
                    continue
                boxIndex= (r//3)*3 + c//3
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in box[boxIndex]:
                    return False
                else:
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    box[boxIndex].add(board[r][c])
        return True



        