class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = set()
        res = 0
        def dfs(i):
            visit.add(i)
            for j in adj[i]:
                if j not in visit:
                    dfs(j)
            
            
        
        for i in range(n):
            if i not in visit:
                res += 1
            dfs(i)
        return res
