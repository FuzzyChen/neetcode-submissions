class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
        "]":"[",
        ")":"(",
        "}":"{"
        }
        stack = []
        for ch in s:
            if ch not in dic:
                stack.append(ch)
            else:
                if not stack or stack.pop() != dic[ch]:
                    return False
                    
        return not stack




        