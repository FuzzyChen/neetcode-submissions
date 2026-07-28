class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            last = stones.pop()
            secondlast = stones.pop()
            cur = last-secondlast
            if cur:
                stones.append(cur)
        return stones[0] if stones else 0
