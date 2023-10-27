#User function Template for python3

class Solution:
    def minimumNumberOfDeletions(self,S):
        # code here 
        n = len(S)
    
        # Create a 2D table to store the minimum number of deletions
        dp = [[0] * n for _ in range(n)]
        
        # Fill in the table using dynamic programming
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if S[i] == S[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])
        
        # The minimum number of deletions to make it a palindrome is in dp[0][n - 1]
        return dp[0][n - 1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
# } Driver Code Ends