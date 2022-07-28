class ClimbingStairs:
    """
    Desc:
        # 70
        You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    Link: 
        https://leetcode.com/problems/climbing-stairs/
    Notes:
    """

    # standard dp
    # Time: O(n) - number of steps 
    # Space: O(n)
    def solution1(n):
        # reaching n options are reaching [n - 1] + [1steps] + n - 2 + [2steps]
        dp = []
        # 1 step stair, dp[0] = 1 
        dp.append(1)
        # 2 step start, dp[1] = 2
        dp.append(2)
        
        # main logic 
        for i in range(2, n):
            dp.append( dp[i-2] + dp[i-1] ) # dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n-1]
