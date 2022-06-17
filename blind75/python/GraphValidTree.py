class GraphValidTree:
    """
    Desc:
        # 261
        Return true if the edges of the given graph make up a valid tree, and false otherwise.
    Link: 
        https://leetcode.com/problems/graph-valid-tree/
    Notes:
    """

    # dfs with prev check
    # tree is valid if all nodes are connect and there are no cycles 
    # Time: O(e+v)
    # Space: O(e+v)
    def validTree(self, n, edges):        
        # empty is a tree
        if not n: 
            return True
        
        # adj list
        adj = { i:[] for i in range(n) }
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        # dfs 
        visited = set()
        # prev holds where it came from, for undirected  
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj[node]:
                # check parent/prev
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
                    
        # check valid
        return dfs(0,-1) and n == len(visited)



    # name
    # Time: O()
    # Space: O()
    def solution2():
        pass