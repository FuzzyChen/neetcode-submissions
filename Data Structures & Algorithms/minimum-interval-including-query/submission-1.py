class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #sort 
        intervals.sort(key = lambda x: (x[0],x[1]-x[0]))
        res = [-1] * len(queries)

        sorted_queries = sorted((q,i) for i,q in enumerate(queries))
        heap = []
        j = 0

        for q,i in sorted_queries:
            while j<len(intervals) and intervals[j][0]<=q:
                start,end = intervals[j]
                l = end -start +1 
                heapq.heappush(heap,(l,end))
                j += 1
            
            while heap and heap[0][1]<q:
                heapq.heappop(heap)
            if heap:
                res[i] = heap[0][0]
        return res
        