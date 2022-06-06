from collections import defaultdict

class GroupAnagrams:
    """
    Desc:
        # 49
        Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    Link: 
        https://leetcode.com/problems/group-anagrams/
    Notes:
        - use ord() to create freq list, ord returns unicode int value
    """

    # hmap with sort letters as key
    # Time: O(N * M logM), N = length of strs, M = largest length of str
    # Space: O(N*M)
    def solution1(self, strs):
        charMap = {}

        for s in strs:
            key = "".join(sorted(s)) # sorted() returns a list, keys can't be list
            if key in charMap:
                charMap[key].append(s)
            else:
                charMap[key] = [s]

        return charMap.values()

    # hmap with freq list as key
    # Time: O(N*M), N = length of strs, M = largest size of str
    # Space: O(N*M)
    def solution2(self, strs):
        charMap = defaultdict(list) # defaults to [] when no keys exist

        for s in strs:
            freqCount = [0] * 26
            for ch in s:
                freqCount[ord(ch)-ord('a')] += 1
            charMap[tuple(freqCount)].append(s) # list can't be keys

        return charMap.values()