class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS= len(text1),len(text2)
        dp = [[0 for _ in range(COLS)] for _ in range(ROWS) ]

        for i in range(ROWS):
            for j in range(COLS):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + (0 if i==0 or j==0 else dp[i-1][j-1])
                else:
                    topVal = 0 if i==0 else dp[i-1][j]
                    leftVal = 0 if j==0 else dp[i][j-1]
                    dp[i][j] = max(topVal,leftVal)
                

        return dp[ROWS-1][COLS-1] 