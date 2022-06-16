class ValidateBinarySearchTree:
    """
    Desc:
        # 98
        Given the root of a binary tree, determine if it is a valid binary search tree (BST).
    Link:
        https://leetcode.com/problems/validate-binary-search-tree/
    Notes:
    """

    # recursive valid range traversal 
        # check left and right bonds for children nodes
        # empty child node is always valid 
        # left < at.val, right > at.val, cannot =
    # Time: O(n)
    # Space: O(n)
    def isValidBST(self, root):

        def valid(node, lowerLimit, upperLimit):
            if not node: return True
            # not valid, (node.val <= lowerLimit or node.val >= upperLimit)
            if not (node.val > lowerLimit and node.val < upperLimit): return False
            
            return valid(node.left, lowerLimit, node.val) and valid(node.right, node.val, upperLimit)
        
        return valid(root, float('-inf'), float('inf'))


    # name
    # Time: O()
    # Space: O()
    def solution2():
        pass