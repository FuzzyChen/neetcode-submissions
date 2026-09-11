class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        x,y = set(),set()
        ROWS, COLS = len(matrix), len(matrix[0])
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    x.add(i)
                    y.add(j)
        for i in x:
            for j in range(COLS):
                matrix[i][j] = 0
        for j in y:
            for i in range(ROWS):
                matrix[i][j] = 0
        