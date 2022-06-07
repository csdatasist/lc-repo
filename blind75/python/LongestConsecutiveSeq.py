class LongestConsecutiveSequence:
    """
    Desc:
        # 128
        Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
    Link: 
        https://leetcode.com/problems/longest-consecutive-sequence/
    Notes:
        - check len 0 edge case
        - use set to optimize
    """

    # sort - sort numbers, store longest by checking last num + 1 = curr num, skip repeating numbers, return max(curr, long) long may not have updated  
    # Time: O(n log n), n = length of nums
    # Space: O(1)
    def solution1(self, nums):
        if len(nums) == 0:
            return 0
        
        long, curr = 1, 1
        nums.sort()

        for i in range(1, len(nums)):
            # repeat go next
            if nums[i] == nums[i-1]:
                continue

            # consective, add to curr
            if nums[i] == nums[i-1]+1:
                curr += 1
            else:
                long = max(curr, long)
                curr = 1
        
        return max(curr, long)


    # using set, find starts and count the length till ends  
    # <---[3,4,5]-------[70,80]------[100]->
    # look for length of longest sequence
    # start of seq is (n-1) not in set
    # end of seq is (n+1) not in set 
    # Time: O(n), number of nums
    # Space: O(n), size of nums
    def solution2(self, nums):
        numSet = set(nums)
        longest = 0

        for n in nums:
            # start of seq
            if (n-1) not in numSet:
                length = 1
                # increment length until end 
                while (n+1) in numSet:
                    length += 1
                    n += 1
                longest = max(length, longest)

        return longest

    # set - same as above shorten length calc
    def solution3(self, nums):
        numSet = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in numSet:
                length = 0
                while n + length in numSet:
                    length += 1
                longest = max(length, longest)

        return longest
