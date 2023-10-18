#User function Template for python3

from typing import List

class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        def is_safe(node):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False
    
            state[node] = 2
            for neighbor in adj[node]:
                if not is_safe(neighbor):
                    return False
            state[node] = 1
            return True
    
        state = [0] * V  # 0: unvisited, 1: safe, 2: unsafe
        safe_nodes = []
    
        for node in range(V):
            if is_safe(node):
                safe_nodes.append(node)
    
        return sorted(safe_nodes)
        # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends