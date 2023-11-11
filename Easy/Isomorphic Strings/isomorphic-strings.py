#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        if len(str1) != len(str2):
            return False
    
        # Create dictionaries to store mappings for each string
        mapping_str1 = {}
        mapping_str2 = {}
    
        # Iterate through each character in both strings
        for char1, char2 in zip(str1, str2):
            # Check mapping for str1
            if char1 in mapping_str1:
                if mapping_str1[char1] != char2:
                    return False
            else:
                mapping_str1[char1] = char2
    
            # Check mapping for str2
            if char2 in mapping_str2:
                if mapping_str2[char2] != char1:
                    return False
            else:
                mapping_str2[char2] = char1
    
        # If the loop completes without returning False, the strings are isomorphic
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends