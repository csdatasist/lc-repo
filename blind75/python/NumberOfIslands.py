from collections import deque

class NumberOfIslands:
    """
    Desc:
        # 200
        Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands. 
    Link: 
        https://leetcode.com/problems/number-of-islands/
    Notes:
    """

    # iterative - search thur grid for island (1), bfs thur island(1), store visited, add island count, continue ignore visited 
    # Time: O(r * c), r = rows, c = cols
    # Space: O(r * c)
    def solution1(grid):
        res = 0
        visited = set()
        
        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            
            while q:
                row, col = q.popleft()
                # up, down, left, right 
                directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # add to q, if in range, gridrc == 1, and havent been visted 
                    if r in range(len(grid)) and c in range(len(grid[r])) and grid[r][c] == "1" and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))
             
        # search all grid for islands, bfs for connected island    
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    res += 1
                    
        return res 


    # recursive, dfs
    # Time: O(r * c)
    # Space: O(r * c)
    def numIslands(self, grid):
        
        islands = 0
        visited = set()
        
        # create traversal algo 
        def traverse(r, c):
            if (r, c) in visited: return 0
            if grid[r][c] == '0': return 0
            
            visited.add((r, c))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                nR, nC = dr + r, dc + c 
                if nR in range(len(grid)) and nC in range(len(grid[nR])):
                    traverse(nR, nC)
            return 1
        
        # traverse grid
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                islands += traverse(r, c)
        
        return islands