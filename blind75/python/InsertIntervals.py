class LC:
    """
    Desc:
        # 57
        Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
    Link: 
        https://leetcode.com/problems/insert-interval/
    Notes:
    """

    # name
    # Time: O(n) - one pass
    # Space: O(n) - results 
    def solution1(self, intervals, newInterval):
        # traverse thur intervals
        # create results to store intervals processed, there will be two sides: res and rest of intervals 
        # cases for newInt: 
        #   goes before intervals -> add to results, return res + rest of intervals
        #   goes in -> merge current int, continue, lots of conditions best to put in else
        #   goes after -> append to at the end 
        
        res = []
        
        for i in range(len(intervals)):
            newStart, newEnd = newInterval
            curStart, curEnd = intervals[i]
            # before:
            if newEnd < curStart:
                res.append(newInterval)
                return res + intervals[i:]
            # after:
            elif newStart > curEnd:
                res.append(intervals[i])
            # overlaps
            else:
                newInterval = [min(newStart, curStart), max(newEnd, curEnd)]
        
        res.append(newInterval)
        return res
