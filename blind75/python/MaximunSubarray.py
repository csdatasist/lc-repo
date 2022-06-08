class MaximumSubarray:
    """
    Desc:
        # 53
        Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    Link: 
        https://leetcode.com/problems/maximum-subarray/
    Notes:
    """

    # go thur nums, keep track of current sum, keep the bigger of curr_sum or curr num
    # Time: O(n)
    # Space: O(1)
    def solution1(self, nums):
        max_sum, cur_sum = nums[0], nums[0]
        
        for n in nums[1:]:
            cur_sum = max(cur_sum + n, n)
            max_sum = max(cur_sum, max_sum)
        
        return max_sum


    # name
    # Time: O()
    # Space: O()
    def solution2():
        pass