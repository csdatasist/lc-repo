class LC:
    """
    Desc:
        # 3
        Given a string s, find the length of the longest substring without repeating characters.
    Link: 
        https://leetcode.com/problems/longest-substring-without-repeating-characters/
    Notes:
    """

    # two pointers, set
        # start two pointers at beginning and traverse right till end
        # create set to store chars, when repeat found move left pointer, remove from set until until repeat is gone
    # Time: O(n) - len of str
    # Space: O(n) - set size
    def solution1(self, s):
        max_len, cur_len = 0, 0 
        l, r = 0, 0
        charSet = set()
        
        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
                cur_len -= 1
                
            charSet.add(s[r])
            r += 1
            cur_len += 1
            max_len = max(max_len, cur_len)
            
        return max_len


    # brute force - check all subtring, check if they have repeats, store max len
    # Time: O(n^3)
    # Space: O()
    def solution1():
        pass