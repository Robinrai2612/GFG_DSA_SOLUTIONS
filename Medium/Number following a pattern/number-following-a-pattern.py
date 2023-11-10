#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,S):
        # code here 
        n = len(S)
        cnt = 1
        ans = [''] * (n + 1)
    
        for i in range(n + 1):
            if i == n or S[i] == 'I':
                # Iterate backward for every 'I'
                j = i - 1
                while j >= -1:
                    ans[j + 1] = str(cnt)
                    cnt += 1
                    if j >= 0 and S[j] == 'I':
                        # Break as soon as 'I' is found while iterating back
                        break
                    j -= 1
        return ''.join(ans)
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends