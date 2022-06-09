class MergeIntervals:
    """
    Desc:
        # 56
        Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
    Link: 
        https://leetcode.com/problems/merge-intervals/
    Notes:
    """

    # sort, create results arr and add first val of intervals, use to look up last int to compare , traverse and merge when overlaps
    # Time: O(nlogn) - sorting
    # Space: O(n) - depends on sorting
    def solution1(self, intervals):
        intervals.sort()
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            # overlaps
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
        
        return res


    # same as above cleaned
    # Time: O(n)
    # Space: O(n)
    def solution2(self, intervals):
        intervals.sort()
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            lastStart, lastEnd = res[-1]
            if lastEnd >= start:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append(intervals[i])
                
        return res