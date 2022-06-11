class LongestRepeatingCharacterReplacement:
    """
    Desc:
        # 424
        You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
    Link: 
        https://leetcode.com/problems/longest-repeating-character-replacement/
    Notes:
    """

    # sliding windows
        # hashset to keep track of max count of chars 
        # window is: length of substring - max char <= replacement
        # (r-l+1) - max(count.values()) <= k
        # meaning when window is not meeting, we increment left pointer and remove
    # Time: O(n)
    # Space: O(n)
    def solution1(s, k):        
        l, r = 0, 0 
        res = 0
        count = {}
        
        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max((r-l+1), res)
            r += 1 
            
        return res


    # name
    # Time: O()
    # Space: O()
    def solution2():
        pass