class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isPermutation(s1,s2):
            return "".join(sorted(s1)) == "".join(sorted(s2))
        
        l1 = len(s1)

        for i in range(len(s2)-l1+1):
            if isPermutation(s1,"".join(s2[i:i+l1])):
                return True
        return False