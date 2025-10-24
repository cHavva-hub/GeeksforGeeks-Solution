# Krishiv Gupta
# ME25B063
# 24 - 10 - 2025

class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        from collections import deque
        
        
        V = len(adj)
        visited = [False] * V
        src = 0
        res = []
        
        q = deque()
        visited[src] = True
        q.append(src)
        
        while q:
            curr = q.popleft()
            res.append(curr)
            
            for x in adj[curr]:
                if not visited[x]:
                    q.append(x)
                    visited[x] = True
                    
        return res
                
