class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)
        sortedS1 = "".join(sorted(s1))
        for i in range(len(s2)-windowSize+1):
            s = s2[i:(i+windowSize)]
            sortedS = "".join(sorted(s))
            if(sortedS == sortedS1):
                return True
        return False
        