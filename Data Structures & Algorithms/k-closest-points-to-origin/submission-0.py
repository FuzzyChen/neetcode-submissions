class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointsWithDistance = list(map(lambda x: [x[0],x[1],x[0] **2 + x[1] **2],points))
        pointsWithDistance.sort(key=lambda x: x[2])
        res = list(
            map(lambda x: [x[0], x[1]], pointsWithDistance)
        )
        return res[:k]