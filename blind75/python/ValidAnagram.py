class ValidAnagram:
    """
    Desc:
        # 242
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    Link: 
        https://leetcode.com/problems/valid-anagram/
    Notes:
    """

    # sorting - sort letters, check if same
    # Time: O(nlogn)
    # Space: O(1)
    def solution1(s, t):
        return sorted(s) == sorted(t)


    # hashmap
    # Time: O(n) - iterating thru both strings & map
    # Space: O(n) - size of map 
    def solution2(s, t):
        # edge: lengths have to be same for anagram
        if len(s) != len(t):
            return False
        
        # create count of letter in string s
        charCount = {}
        for ch in s:
            charCount[ch] = charCount.get(ch, 0) + 1

        # check letters that don't exist / no longer exist in string t
        # decrease count of t
        for ch in t:
            if ch not in charCount or charCount[ch] == 0:
                return False
            else:
                charCount[ch] -= 1 
            
        return True


    # freqency counter - create freq list, add/minus s and t same time, check freq list for non zeros
    # Time: O(n)
    # Space: O(1)
    def solution3(s, t):
        pass