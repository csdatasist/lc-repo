class ThreeSum:
    """
    Desc:
        # 15
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Link: 
        https://leetcode.com/problems/3sum/
    Notes:
        - watch for dups
    """

    # two pointer - sort, linear serach and two pointers
    # Time: O(n^2)
    # Space: O(1)
    def solution1(self, nums):
        res = [] 
        nums.sort()
        
        for i in range(len(nums)):
            # skip dups
            if nums[i] == nums[i-1] and i > 0:
                continue
            
            l, r = i+1, len(nums)-1
            
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if sum3 == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # skip dups
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif sum3 < 0:
                    l += 1
                else:
                    r -= 1
                    
        return res

    # name
    # Time: O()
    # Space: O()
    def solution2():
        pass