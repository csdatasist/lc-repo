class MeetingRoomsII:
    """
    Desc:
        # 253
        Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
    Link: 
        https://leetcode.com/problems/meeting-rooms-ii/
        https://www.lintcode.com/problem/919/
    Notes:
    """

    # create list of start times and end times
        # sort them
        # traverse them in order, 
        # start time mean rooms is need +1, end time means room is open -1
        # track max rooms needed till start times empty, no more start times means no more rooms needed
    # Time: O(nlogn) - sorting
    # Space: O(n) - creating 2 new list of size n
    def solution1(self, intervals):
        res, rooms = 0, 0
        
        startTimes, endTimes = [], []
        for start, end in intervals:
            startTimes.append(start)
            endTimes.append(end)
        startTimes.sort()
        endTimes.sort()
        
        while startTimes:
            if startTimes[0] < endTimes[0]:
                startTimes.pop(0)
                rooms += 1
                res = max(res, rooms)
            else:
                endTimes.pop(0)
                rooms -= 1
            
        return res 


    # priority queues
    # Time: O()
    # Space: O()
    def solution2():
        pass