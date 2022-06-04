class ContainsDuplicate:
    """
    Desc:
        # 217
        Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
    Link: 
        https://leetcode.com/problems/contains-duplicate/
    Notes:
        - use a set
    """

    # brute force - linear search
    # time: O(n^2) - loops n * n-1
    # space: O(1) - constant
    def solution1(self, nums):
        # look at each number, check for repeat in rest of list
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
                
        return False

    # hashset
    # time: O(n) - stores nums in set, 1 pass thur
    # space: O(n) - set can hold up to n values
    def solution2(self, nums):
        seen = set()    
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        
        return False
