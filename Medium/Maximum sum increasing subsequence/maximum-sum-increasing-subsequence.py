#User function Template for python3
class Solution:
	def maxSumIS(self, Arr, n):
	    dp = [0] * n

        for i in range(n):
            dp[i] = Arr[i]
    
        for i in range(1, n):
            for j in range(i):
                if Arr[i] > Arr[j] and dp[i] < dp[j] + Arr[i]:
                    dp[i] = dp[j] + Arr[i]
    
        return max(dp)
	        
	    
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends