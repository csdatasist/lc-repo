class ProductofArrayExceptSelf:
    """
    Desc:
        # 238
        Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
    Link: 
        https://leetcode.com/problems/product-of-array-except-self/
    Notes:
    """

    # left and right product list - get list of left products and right products, then mutiply together 
    # Time: O(n) - length of nums
    # Space: O(n) - two product arrays
    def solution1(self, nums):
        res = [0] * len(nums)

        # left side
        product = 1
        for i in range(len(nums)):
            res[i] = product
            product *= nums[i]

        # right side
        product = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= product
            product *= nums[i]

        return res

    # name
    # Time: O()
    # Space: O()
    def solution2():
        pass