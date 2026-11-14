class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = zip(position,speed)
        stack = []
        for (p,s) in sorted(pair)[::-1]:
            leftTime = (target-p)/s
            if not stack or stack[-1] < leftTime:
                stack.append(leftTime)
        return len(stack)


        