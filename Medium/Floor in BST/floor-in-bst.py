#User function Template for python3

class Solution:
    def floor(self, root, x):
        if root is None:
            return -1  # If the tree is empty
    
        floor_val = -1  # Initialize with -1 as a default value
    
        while root:
            if root.data == x:
                return root.data  # Exact match found
            elif root.data < x:
                floor_val = root.data
                root = root.right
            else:
                root = root.left
    
        return floor_val
        
        # Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def insert(tree, val):
    if(tree==None):
        return Node(val)
    if(val< tree.data):
        tree.left= insert(tree.left, val)
    elif(val > tree.data):
        tree.right= insert(tree.right, val)
    return tree
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr= list(map(int, input().split()))
        root = None
        for k in arr:
            root=insert(root, k)
        s=int(input())
        obj = Solution()
        print(obj.floor(root,s))
# } Driver Code Ends