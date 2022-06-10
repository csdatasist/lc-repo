class SearchinRotatedSortedArray:
    """
    Desc:
        # 33
        Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
    Link: 
        https://leetcode.com/problems/search-in-rotated-sorted-array/
    Notes:
    """

    # binary search on two sides of pivot
    # Time: O(logn)
    # Space: O(1)
    def solution1(nums, target):
        def findPivot(nums):
            l, r = 0, len(nums)-1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        piv = findPivot(nums)
        
        # search left
        l, r = 0, piv-1
        while l <= r:
            m = (l + r) // 2
            if nums[m]  == target:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        
        # search right
        l, r = piv, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            if nums[m]  == target:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        
        return -1



    # name
    # Time: O()
    # Space: O()
    def solution2():
        pass