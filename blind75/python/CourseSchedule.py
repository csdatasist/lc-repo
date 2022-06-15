from collections import defaultdict


class CourseSchedule:
    """
    Desc:
        # 207
        Return true if you can finish all courses. Otherwise, return false
    Link:
        https://leetcode.com/problems/course-schedule/
    Notes:
    """

    # dps from neetcode
    # Time: O(n+p), n = nodes, p=prereq/edges
    # Space: O(n)
    def solution1(self, numCourses, prerequisites):
        # create adjacy list
        adj = defaultdict(list) # adj={i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        # check if finish able, dfs
        visited = set()
        def completable(crs):
            if crs in visited: return False #theres a cycle 
            if adj[crs] == []: return True #crs has no prereqs
            
            visited.add(crs)
            for pre in adj[crs]:
                if not completable(pre): return False
            visited.remove(crs)
            adj[crs] = [] 
            return True
            
        # check all class to be completable
        for c in range(numCourses):
            if not completable(c): return False
        
        return True


    # name
    # Time: O()
    # Space: O()
    def solution2():
        pass