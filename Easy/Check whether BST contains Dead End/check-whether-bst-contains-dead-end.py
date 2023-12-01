# Your task is to complete this function
# function should return true/false or 1/0
class Solution:
    def storeNodes(self, root, st, leafset):
        if root is None:
            return
        
        st.add(root.data)
        if root.left is None and root.right is None:
            leafset.add(root.data)
            return
        
        self.storeNodes(root.left, st, leafset)
        self.storeNodes(root.right, st, leafset)
    def isDeadEnd(self, root):
        # Code here
        if not root:
            return True
        
        st = {0}
        leafset = set()
        self.storeNodes(root, st, leafset)
        
        for x in leafset:
            if x + 1 in st and x - 1 in st:
                return True
        
        return False
        



#{ 
 # Driver Code Starts

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.data == node.data:
            return
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        root = None
        for j in arr:
            if root is None:
                root = Node(j)
            else:
                insert(root, Node(j))
                
        ob = Solution()
        if ob.isDeadEnd(root):
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends