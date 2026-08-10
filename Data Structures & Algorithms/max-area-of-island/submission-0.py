class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROW,COL = len(grid),len(grid[0])
        visited = set()
        def dfs(r,c):
            if r<0 or c<0 or r>=ROW or c>=COL or grid[r][c] == 0 or (r,c) in visited:
                return 0
            if grid[r][c] == 1:
                visited.add((r,c))
                return dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1) + 1
                

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    res = max(res,area)

        return res