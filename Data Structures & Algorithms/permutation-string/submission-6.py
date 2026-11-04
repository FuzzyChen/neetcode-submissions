class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count1 = [0] *26
        count2 = [0] *26
        l1 = len(s1)
        if(len(s2) < l1):
            return False
        for i in range(l1):
            count1[ord(s1[i])-ord('a')] += 1
            count2[ord(s2[i])-ord('a')] += 1
        if count1 == count2:
            return True
        for i in range(len(s2)-l1):
            count2[ord(s2[i])-ord('a')] -= 1
            count2[ord(s2[i+l1])-ord('a')] += 1
            if(count1==count2):
                return True
        return False