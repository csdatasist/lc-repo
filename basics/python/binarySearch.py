class BinarySearch:
    """
    Binary Search
    """

    # Time: O(logn)
    # Space: O(1)
    def solution1(self, nums, target):
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right - left) // 2  #(l + r)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        return -1 

