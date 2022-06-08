class MeetingRooms:
    """
    Desc:
        # 252
        Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
    Link: 
        https://leetcode.com/problems/meeting-rooms/
        https://www.lintcode.com/problem/920/
    Notes:
    """

    # sort, check if curr end time intercepts with next start time
    # Time: O(nlogn)
    # Space: O(1)
    def solution1(self, intervals):
        intervals.sort()
        
        for i in range(len(intervals)-1):
            # start int[i][0], end int[i][1]
            if intervals[i][1] > intervals[i+1][0]:
                return False
            
        return True


    # bruce force - check all time for intersections 
    # Time: O(n^2)
    # Space: O(1)
    def solution2():
        pass
