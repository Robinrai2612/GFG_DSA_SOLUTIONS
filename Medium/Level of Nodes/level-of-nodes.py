#User function Template for python3
from collections import deque
class Solution:
    
    #Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        visited = [False] * V
        level = 0
        queue = deque([0])
    
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                current_node = queue.popleft()
    
                if current_node == X:
                    return level
    
                for neighbor in adj[current_node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
    
            level += 1
    
        return -1  # X is not found
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
        X=int(input())
        ob = Solution()
        
        print(ob.nodeLevel(V, adj, X))
# } Driver Code Ends