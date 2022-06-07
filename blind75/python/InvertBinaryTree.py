class InvertBinaryTree:
    """
    Desc:
        # 226
        Given the root of a binary tree, invert the tree, and return its root.
    Link: 
        https://leetcode.com/problems/invert-binary-tree/
    Notes:
    """

    # recursive
    # Time: O(n)
    # Space: O(n), n = num of nodes
    def invertTree(self, root):
        if not root:
            return None
        
        # shortcut root.left, root.right = root.right, root.left
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


    # iterative
    # Time: O(n)
    # Space: O(n)
    def solution2():
        pass