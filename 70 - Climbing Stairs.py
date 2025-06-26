class Solution:
    def climbStairs(self, n: int) -> int:
        dp={}
        def backtrack(i):
            
            if i==n-1:
                return 1
            if i== n-2:
                return 2
            if i in dp:
                return dp[i]
            dp[i] = backtrack(i+1) + backtrack(i+2)
            return dp[i]
        return backtrack(0)

        
