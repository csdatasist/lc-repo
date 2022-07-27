class HouseRobberII:
    """
    Desc:
        # 213
        Same as house robber I with circle arrangement
    Link: 
        https://leetcode.com/problems/house-robber-ii/
    Notes:
    """

    # dp, same as 1 but split into two nums
    # Time: O(n)
    # Space: O(1)
    def solution1(nums):
        def houserob1(nums):
            if not nums: return 0
            rob1, rob2 = 0, 0
            for n in nums:
                temp = rob2
                rob2 = max(rob1 + n, rob2)
                rob1 = temp
            return rob2

        if len(nums) == 1: return nums[0] # remember size of 1, can also add to max(nums[0],..,..)
        return max( houserob1(nums[:-1]), houserob1(nums[1:]) ) # nums[:-1] -> start to 1 b4 end, [1:] -> second to end 


