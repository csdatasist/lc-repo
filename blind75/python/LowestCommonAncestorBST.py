class LC:
    """
    Desc:
        # 235
        Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
    Link: 
        https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
    Notes:
    """

    # iterative
        # bst - left children are less and right children are greater 
        # lca happens when p and q are on opposite sides of the root
        # traverse bst comparing p and q until they are on opposite sides
    # Time: O(n), n = num of nodes
    # Space: O(1)
    def solution1(root, p, q):
        curr = root
        while curr:
            # both val on left
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # both val on right
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # split, meaning lca
            else: 
                return curr


    # name
    # Time: O()
    # Space: O()
    def solution2():
        pass