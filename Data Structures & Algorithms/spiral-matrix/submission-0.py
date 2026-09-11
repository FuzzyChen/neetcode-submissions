class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        res = []
        r,c = 0,0
        nextD = 0
        ROWS = len(matrix)
        COLS = len(matrix[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        while 0<=r<ROWS and 0<=c<COLS and not visited[r][c]:
            res.append(matrix[r][c])
            visited[r][c] = True
            dr,dc = directions[nextD % 4]
            nr,nc = r+dr, c+dc
            if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or visited[nr][nc]:
                nextD += 1
                dr, dc = directions[nextD % 4]
                nr, nc = r + dr, c + dc
            r = nr
            c = nc
        
        return res
