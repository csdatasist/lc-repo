class ContainerWithMostWater:
    """
    Desc:
        # 11
        You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Link: 
        https://leetcode.com/problems/container-with-most-water/
    Notes:
        - two pointers
        - area = min(left_height, right_height) * right_index - left_index
    """

    # bruce force - calc every possible container
    # Time: O(n^2)
    # Space: O(1)
    def solution1():
        pass


    # two pointers - calc the max of water going inwards, move the smaller pointer first
    # Time: O(n)
    # Space: O(1)
    def solution2(self, height):
        curr, maxx = 0, 0 
        l, r = 0, len(height)-1

        while l < r:
            curr = min(height[l], height[r]) * (r - l)
            maxx = max(maxx, curr)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxx
