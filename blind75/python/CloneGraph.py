from collections import deque


class CloneGraph:
    """
    Desc:
        # 133
        Return a deep copy (clone) of the graph.
    Link: 
        https://leetcode.com/problems/clone-graph/
    Notes:
    """

    # iterative - create copys dict, add copy node, bfs thur neighbors creating copies when needed and adding nei to copies neighbors, copies also acts as visited check 
    # Time: O(n+m), n = node, m = edges
    # Space: O(n), n = nodes
    def solution1(self, node):
        if not node:
            return None
        
        copys = {} # key: old node, val: copy of node
        copys[node] = Node(node.val, []) 
        
        que = deque()
        que.append(node)
        
        while que:
            curr = que.pop()
            for nei in curr.neighbors:
                # make copy 
                if nei not in copys:
                    copys[nei] = Node(nei.val, [])
                    que.append(nei) # copys also serves as a visited for cycles 
                # add nei to copy 
                copys[curr].neighbors.append(copys[nei])
        
        return copys[node]


    # recursive 
    # Time: O()
    # Space: O()
    def solution2():
        pass

class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
