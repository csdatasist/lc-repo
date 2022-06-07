class LC:
    """
    Desc:
        # 125
        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. 
    Link: 
        https://leetcode.com/problems/valid-palindrome/
    Notes:
        - use .isalnum()
        - lowercase ch before check
        - watch for out of bonds from non alnum loop too 
    """

    # two pointers - left, right pointers compare for equal, loop to skip non alpha numeric values
    # Time: O(n)
    # Space: O(1)
    def solution1(self, s):
        l, r = 0, len(s)-1

        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True


    # compare reverse str after removing non alpha numeric
    # Time: O(n)
    # Space: O(n)
    def solution2(self, s):
        alnumS = ""
        for ch in s:
            if ch.isalnum():
                alnumS += ch

        return alnumS.lower() == alnumS[::-1].lower()