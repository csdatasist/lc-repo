class DiameterOfBinaryTree:
    """
    Desc:
        # 543
        Given the root of a binary tree, return the length of the diameter of the tree.
    Link: 
        https://leetcode.com/problems/diameter-of-binary-tree/
    Notes:
    """

    # dfs
    # Time: O(n) - nodes in tree
    # Space: O(n)
    def diameterOfBinaryTree(self, root): 
        # the diameter is the longest path b/n any two nodes
        # path is a cnt of edges
        
        res = 0
        
        # for each node get length of left and right path
        # res = max(left + right paths, res)
        
        def maxPath(n):
            if not n: return 0
            
            nonlocal res
            
            # get max paths
            left = maxPath(n.left) 
            right = maxPath(n.right)
            path = 1 + max(left, right)
            
            # check diameter 
            res = max(res, left + right)
        
            return path 
            
        maxPath(root)
        return res


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right