from typing import List

class Solution:
    def largestIsland(self, grid : List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def is_valid(i, j):
            return 0 <= i < m and 0 <= j < n

        def get_neighbors(i, j):
            return [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]

        def dfs(i,j, index):
            grid[i][j] = index
            count = 1
            for nei in get_neighbors(i, j):
                x, y = nei
                if is_valid(x, y) and grid[x][y] == 1:
                    grid[x][y] = index
                    count+=dfs(x,y, index)
            return count

        islands_map = {}
        self.max_len = 0
        water_cells = set()

        index = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    water_cells.add((i,j))
                elif grid[i][j] == 1:
                    size = dfs(i, j, index)
                    islands_map[index] = size
                    self.max_len = max(self.max_len, size)
                    index+=1
        
        for cell in water_cells:
            i, j = cell
            # make it 1 and see, how big island can be formed idxs = set()
            idxs = set()
            island_len = 1
            for nei in get_neighbors(i, j):
                x, y = nei
                if is_valid(x, y) and grid[x][y] in islands_map and grid[x][y] not in idxs:
                    idxs.add(grid[x][y])
                    island_len+=islands_map[grid[x][y]]

            self.max_len = max(self.max_len, island_len)
        return self.max_len
        
        # Code here
        




#{ 
 # Driver Code Starts

class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        grid=IntMatrix().Input(n,n)
        
        obj = Solution()
        res = obj.largestIsland(grid)
        
        print(res)
# } Driver Code Ends