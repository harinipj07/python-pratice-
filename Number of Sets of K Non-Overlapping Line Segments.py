class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [[[-1] * 2 for _ in range(k + 1)] for _ in range(n + 1)]

        def solve(idx, start, k):
            if k == 0:
                return 1
            if idx == n:
                return 0

            if dp[idx][k][start] != -1:
                return dp[idx][k][start]

            ans = 0

            if start:
                ans += solve(idx, 0, k - 1)
                ans += solve(idx + 1, 1, k)
            else:
                ans += solve(idx + 1, 1, k)
                ans += solve(idx + 1, 0, k)

            dp[idx][k][start] = ans % MOD
            return dp[idx][k][start]

        return solve(0, 0, k)
        
