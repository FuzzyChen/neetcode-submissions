class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #pre process
        prereq = { i:[] for i in range(numCourses)}
        for pre,req in prerequisites:
            prereq[pre].append(req)
        
        #visted
        #visting
        #unvisted

        visit, cycle = set(),set()
        res = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
                
            visit.add(crs)
            cycle.remove(crs)
            res.append(crs)

        

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res