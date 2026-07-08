class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        if t == "":
            return ""

        #make count map
        countT, window = {}, {}
        
        l = 0
        res, resLen = [0,0], float("infinity")
        for c in t:
            countT[c] = 1 + countT.get(c,0)
        have, need = 0, len(countT)
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if(c in countT and window[c] == countT[c] ):
                have += 1

            while have == need:
                windowSize = r-l+1
                if windowSize < resLen:
                    res = [l,r]
                    resLen = windowSize
                
                window[s[l]] -= 1 
                if s[l] in countT and window[s[l]]< countT[s[l]]:
                    have -= 1
                l += 1 
        l,r = res
             
        return s[l:r+1] if resLen != float('infinity') else ""
        