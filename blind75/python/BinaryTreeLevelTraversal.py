import collections

class BinaryTreeLevelOrderTraversal:
    """
    Desc:
        # 102
        Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
    Link: 
        https://leetcode.com/problems/binary-tree-level-order-traversal/
    Notes:
    """

    # bfs, get levels with len, add by levels, only add non empty levels 
    # Time: O(n), num of nodes
    # Space: O(n)
    def levelOrder(self, root):
        res = []
        
        q = collections.deque()
        q.append(root)
        
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                curr = q.popleft()
                if curr:
                    level.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if level:
                res.append(level)
                
        return res

