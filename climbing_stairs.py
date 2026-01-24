class Solution:
    def climbStairs(self, n: int) -> int:
        memory = {}

        def dp(n):

            if n in memory:
                return memory[n]
            if n == 1:
                return 1
            if n == 2:
                return 2

            memory[n] =  dp(n-1) + dp(n-2)
            return memory[n]

        return dp(n)
