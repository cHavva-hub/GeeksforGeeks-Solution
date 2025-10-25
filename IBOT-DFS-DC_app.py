# Krishiv Gupta
# ME25B063
# 24 - 10 - 2025


class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        # code here
        V = len(adj)
        visited = [False] * V
        
        src = 0
        res = []
        visited[src] = True
        res.append(src)
        
        def dfs2(node):
            curr = adj[node]
            for x in curr:
                if not visited[x]:
                    res.append(x)
                    visited[x] = True
                    dfs2(x)
        dfs2(src)
        return res
