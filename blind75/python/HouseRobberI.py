class HouseRobber:
    """
    Desc:
        # 198
        Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
    Link: 
        https://leetcode.com/problems/house-robber/
    Notes:
    """

    # standard dp template
    # Time: O(n)
    # Space: O(n)
    def solution1(nums):
        if not nums: return 0
        
        dp = [None for n in range(len(nums)+1)]
        dp[0], dp[1] = 0, nums[0]

        for i in range(1, len(nums)):
            dp[i+1] = max(dp[i], dp[i-1] + nums[i])

        return dp[len(nums)]

    
    # dp optimize for space
    # Time: O(n)
    # Space: O(1)
    def solution2(nums):
        if not nums: return 0
        prev, curr = 0, 0 # prev = b4 best, curr = last best

        for n in nums:
            temp = curr
            curr = max(n + prev, curr)
            prev = temp

        return curr