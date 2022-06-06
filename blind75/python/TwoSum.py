class TwoSum:
    """
    Desc:
        # 1
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    Link: 
        https://leetcode.com/problems/two-sum/
    Notes:
    """

    # brute force - linear search, check every combination of numbers
    # Time: O(n^2)
    # Space: O(1)
    def solution1():
        pass


    # hashmap - store values, then check for complement
    # Time: O(n) 
    # Space: O(n)
    def solution2(self, nums, target):
        hmap = {} # num : index 
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hmap:
                return [i, hmap.get(complement)]
            hmap[nums[i]] = i 