class FindMinimuminRotatedSortedArray:
    """
    Desc:
        # 153
        Given the sorted rotated array nums of unique elements, return the minimum element of this array.
    Link: 
        https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
    Notes:
    """

    # binary search - draw picture showing left sorted and right sorted, move pointed depending on side
    # Time: O(logn)
    # Space: O(1)
    def solution1(self, nums):
        l, r = 0, len(nums)-1

        while l < r:
            mid = (l + r) // 2
            # right side
            if nums[mid] < nums[r]:
                r = mid
            # left side
            else:
                l = mid + 1

        return nums[l]


    # name
    # Time: O()
    # Space: O()
    def solution2():
        pass