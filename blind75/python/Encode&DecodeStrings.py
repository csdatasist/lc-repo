class LC:
    """
    Desc:
        # 271 
        Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
    Link: 
        https://leetcode.com/problems/encode-and-decode-strings/
        https://www.lintcode.com/problem/659/
    Notes:
    """

    # encode with len + delimter, decode start to delimter is len of str, start + 1 + length to get to next str
    # Time: O(n), n = length of strs
    # Space: O(n), n = numbers of strs 
    def solution1():
        def encode(self, strs):
            """Encodes a list of strings to a single string.
            """
            # add len(str) + delimiter + str
            res = ""
            for s in strs:
                res += str(len(s)) + '#' + s
            return res        

        def decode(self, s):
            """Decodes a single string to a list of strings.
            """
            i = 0
            res = []

            while i < len(s):
                # set start
                j = i 

                # look for delimiter
                while s[j] != "#": 
                    j += 1 
                # get len of str "3#foo7#..." every thing before # is the len
                s_len = int(s[i:j])

                # add str "foo" 
                res.append( s[ j+1: j+1+s_len ] )
                # move i to next str, start + 1 + length of str
                i = j+1 + s_len

            return res



    # same as above - cleaned
    # Time: O(n)
    # Space: O(n)
    def solution2(self, s):
        i = 0
        res = []

        while i < len(s):
            j = i 

            while s[j] != "#": 
                j += 1 

            s_len = int(s[i:j])
            res.append( s[ j+1: j+1+s_len ] )
            i = j+1 + s_len

        return res