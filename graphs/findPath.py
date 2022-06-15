class FindPath:
    """
    Desc:
        # 1971
        Find valid path in a bi-directional graph
    Link: 
        https://leetcode.com/problems/find-if-path-exists-in-graph/
    Notes:
    """

    # recursive
    # Time: O(v+e), vertices + edges
    # Space: O(v)
    def solution1(self, n, edges, source, destination):
        # adj list
        adj = { i:[] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        # dfs
        visit = set()
        def dfs(src, des):
            if src == des: return True
            if src in visit: return
            
            visit.add(src)
            for nei in adj[src]:
                if dfs(nei, des): return True
            return False
        
        return dfs(source, destination)


    # iterative
    # Time: O(v+e)
    # Space: O(v)
    def solution2(self, n, edges, source, destination):
        # create adj list
        adj = { i:[] for i in range(n) }
        for u, v in edges: 
            adj[u].append(v)
            adj[v].append(u)
        
        q = [source]
        visited = set()
        
        # bfs
        while q:
            current = q.pop(0)
            if current == destination: return True
            for neighbor in adj[current]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
            
        return False
