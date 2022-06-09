class NonOverlappingIntervals:
    """
    Desc:
        # 435
        Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-ov
    Link: 
        https://leetcode.com/problems/non-overlapping-intervals/
    Notes:
    """

    #   sort, store interval one to compare too
        # traverse checking for overlaps
        # when overlaps, add to cnt and store the min of interval ends (this minize overlaps)
        # else update last intervel with current interval
    # Time: O(nlogn)
    # Space: O(1)
    def solution1(self, intervals):
        intervals.sort()
        res = 0
        
        lastInt = intervals[0]
        for i in range(1, len(intervals)):
            # overlaps
            if lastInt[1] > intervals[i][0]:
                res += 1
                lastInt[1] = min(lastInt[1], intervals[i][1])
            else:
                lastInt[1] = intervals[i][1]
        
        return res


    # cleaned, only need the end of last interval
    # Time: O(nlogn)
    # Space: O(1)
    def solution2(self, intervals):
        intervals.sort()
        lastEnd = intervals[0][1]
        count = 0
        
        for start, end in intervals[1:]:
            if lastEnd > start: 
                count += 1
                lastEnd = min(lastEnd, end)
            else:
                lastEnd = end
            
        return count