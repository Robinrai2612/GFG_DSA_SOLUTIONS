#User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        dp = [0] * (W + 1)  # Initialize a 1D array to store maximum values for each weight

        for w in range(1, W + 1):
            for i in range(N):
                if wt[i] <= w:
                    dp[w] = max(dp[w], dp[w - wt[i]] + val[i])
    
        return dp[W]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends