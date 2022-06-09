class MaximumDepthofBinaryTree:
    """
    Desc:
        # 104
        Given the root of a binary tree, return its maximum depth.
    Link: 
        https://leetcode.com/problems/maximum-depth-of-binary-tree/
    Notes:
    """

    # recursive
    # Time: O(n) - num of nodes
    # Space: O(n) - stack of recursion
    def solution1(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


    # iterative
    # Time: O()
    # Space: O()
    def solution2():
        pass
