#User function Template for python3


class Solution:
    
    #Function to find the nodes that are common in both BST.
    def findCommon(self, root1, root2):
        result = []
        stack1, stack2 = [], []
        
        # Helper function to perform in-order traversal and push nodes to the stack
        def pushAllLeftNodes(node, stack):
            while node:
                stack.append(node)
                node = node.left
        
        pushAllLeftNodes(root1, stack1)
        pushAllLeftNodes(root2, stack2)
        
        while stack1 and stack2:
            node1, node2 = stack1[-1], stack2[-1]
            
            if node1.data == node2.data:
                result.append(node1.data)
                stack1.pop()
                stack2.pop()
                pushAllLeftNodes(node1.right, stack1)
                pushAllLeftNodes(node2.right, stack2)
            elif node1.data < node2.data:
                stack1.pop()
                pushAllLeftNodes(node1.right, stack1)
            else:
                stack2.pop()
                pushAllLeftNodes(node2.right, stack2)
        
        return result
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root1=buildTree(s)
        s=input()
        root2=buildTree(s)
        ob = Solution()
        res = ob.findCommon(root1, root2)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends