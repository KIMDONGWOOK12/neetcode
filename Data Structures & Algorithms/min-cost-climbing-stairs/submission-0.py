class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            from_one = dp[i - 1] + cost[i - 1]
            from_two = dp[i - 2] + cost[i - 2]
            dp[i] = min(from_one, from_two)

        return dp[n]