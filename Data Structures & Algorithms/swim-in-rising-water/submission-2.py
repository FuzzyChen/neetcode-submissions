class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #BFS
        N = len(grid)
        visit = set()
        minH = [[grid[0][0],0,0]]
        visit.add((0,0))
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while minH:
            t,r,c = heapq.heappop(minH)
            if r == N-1 and c == N-1:
                return t
            for dr,dc in directions:
                neir, neic = r+dr, c+ dc
                if (neir == N or neic == N or neic<0 or neir<0 or (neir,neic) in visit):
                    continue
                visit.add((neir,neic))
                heapq.heappush(minH,[max(t,grid[neir][neic]),neir,neic])
