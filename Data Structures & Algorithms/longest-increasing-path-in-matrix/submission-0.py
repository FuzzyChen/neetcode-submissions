class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp  = {} #(i,j) => LIP

        def dfs(i,j,prev):
            if(i>=ROWS or i<0 or j<0 or j>=COLS or matrix[i][j]<=prev):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            
            res = 1
            res = max(res, 1+ dfs(i+1,j,matrix[i][j]))
            res = max(res, 1+dfs(i-1,j,matrix[i][j]))
            res = max(res, 1+dfs(i,j+1,matrix[i][j]))
            res = max(res, 1+dfs(i,j-1,matrix[i][j]))
            dp[(i,j)] = res
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,-1)
        # print(dp)
        return max(dp.values())