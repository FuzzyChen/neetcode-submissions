class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        n = len(s)

        # dp[i] = number of ways to decode first i characters
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):

            # One digit: 1-9
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]

            # Two digits: 10-26
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[n]