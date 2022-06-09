class SubtreeOfAnotherTree:
    """
    Desc:
        # 572
        Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
    Link: 
        https://leetcode.com/problems/subtree-of-another-tree/
    Notes:
    """

    # recursive 
    # Time: O(n * m), n = size of root, m = size of sub
    # Space: O(n * m)
    def isSametree(self, root, subRoot):
        # check case: subRoot is none -> true, root is noen -> false, 
        # check root and each subroot of root to see if same given subroot
        # create sameTree check
        
        def isSame(p, q):
            if not p and not q: return True
            if not p or not q: return False
            if p.val != q.val: return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        
        if not subRoot: return True
        if not root: return False
        if isSame(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    # name
    # Time: O()
    # Space: O()
    def solution2():
        pass