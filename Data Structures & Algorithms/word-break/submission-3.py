class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}

        def dfs(s):
            if not s:
                return True

            if s in memo:
                return memo[s]

            for i in range(len(s)):
                if s[:i+1] in wordDict:
                    if dfs(s[i+1:]):
                        # memo[s] = True
                        return True

            memo[s] = False
            return False

        return dfs(s)