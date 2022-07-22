class NumberOfOneBits:
    """
    Desc: 
        # 191 
        Write a function that takes an unsigned integer and returns the number of '1' bits it has
    Link: 
        https://leetcode.com/problems/number-of-1-bits/
    Notes:
        - hammingtons weigth 
    """

    # mod (%) and right shift (>>) 
    # Time: O(32)
    # Space: O(1)
    def solution1(n):
        cnt = 0
        while n > 0:
            if n % 2 == 1: cnt += 1
            n = n >> 1
        
        return cnt

