class MissingNumber:
    """
    Desc:
        # 268
        Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
    Link:
        https://leetcode.com/problems/missing-number/ 
    Notes:
    """

    # use set
    # Time: O(n), size of nums
    # Space: O(n)
    def solution1(nums):
        numSet = set(nums)
        
        for n in range(len(nums)+1):
            if n not in numSet:
                return n


    # math
    # add all range [0, 1, 2, 3]
    # sub all nums [0, 1, 3]
    # Time: O(n)
    # Space: O(1)
    def solution2(nums):
        # math
        # add all range [0, 1, 2, 3]
        # sub all nums [0, 1, 3]
        res = len(nums) # needed for last range
        for i in range(len(nums)):
            res += (i - nums[i])
        return res

    # binary
    # XOR - xor cancels out numbers in binary no matter the order 
    def solution3(nums):
        res = len(nums)
        for i, num in enumerate(nums):
            res = res ^ i ^ num
        return res