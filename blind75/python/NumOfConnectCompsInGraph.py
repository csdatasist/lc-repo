class NumberOfConnectedComponentsInUndirectedGraph:
    """
    Desc:
        # 323
        Return the number of connected components in the graph.
    Link:
        https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
    Notes:
    """

    # union find  
    # Time: O(e)
    # Space: O(v)
    def solution1(self, n, edges):
        parent = [i for i in range(n)] # the root/parent node  
        rank = [1] * n # size of connects
        
        # finds the parent
        def find(n1):
            res = n1

            # continue until parent is parent of itself
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        # connects node when parents arent the same
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            # rank to optimize
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1

        # components start at n, each connections decre by 1 
        res = n 
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res


    # adj list, dfs
    # Time: O(e + v), edges + vertices
    # Space: O(v)
    def solution2(self, n, edges):
        # adj list
        adj = {i:[] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        print(adj)
        
        visit = set()
        
        # dfs, explore all components, return true if explored
        def explore(vertex):
            if vertex in visit: 
                return False
            
            visit.add(vertex)
            for nei in adj[vertex]:
                explore(nei)
            
            return True
            
        # dfs on each ver, explore means new component 
        res = 0
        for v in range(n):
            if explore(v):
                res += 1
            
        return res