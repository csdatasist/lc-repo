from collections import deque


class SameTree:
    """
    Desc:
        # 100
        Given the roots of two binary trees p and q, write a function to check if they are the same or not.
    Link: 
        https://leetcode.com/problems/same-tree/
    Notes:
    """

    # iterative
    # Time: O(n)
    # Space: O(n)
    def solution1(self, p, q):
        pass

    # recursive, both none is true, false is different values or one is none
    # Time: O(n) - n = nodes 
    # Space: O(n) - worse o(n), best o(logn)
    def isSameTree(self, p, q):
        # both None
        if not p and not q:
            return True
        
        # one is none or vals are not same
        if not p or not q or p.val != q.val:
            return False
        
        # check both sides recursively
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)