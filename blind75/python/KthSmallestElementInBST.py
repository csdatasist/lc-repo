class LC:
    """
    Desc:
        # 230
        Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
    Link: 
        https://leetcode.com/problems/kth-smallest-element-in-a-bst/
    Notes:
    """

    # inorder traversal, left mid right 
    # use stack, go most left first
    # Time: O()
    # Space: O()
    def solution1(self, root, k):  
        stack = []
        cur = root
        cnt = 0
        
        while stack or cur:
            # cur is most left
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # process node, check if kth value
            cur = stack.pop()
            cnt += 1
            if cnt == k: return cur.val
            
            cur = cur.right # add right last  


    # name
    # Time: O()
    # Space: O()
    def solution2():
        pass