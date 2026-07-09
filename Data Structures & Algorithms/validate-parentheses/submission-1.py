class Solution:
    def isValid(self, s: str) -> bool:
        
        dic = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        res = []
        for  ch in s:
            if ch in dic:
                if not res:
                    return False
                current = res.pop()
                if current != dic[ch]:
                    return False
            else:
                res.append(ch)
        return  len(res) == 0

        