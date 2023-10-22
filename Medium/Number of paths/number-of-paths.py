#User function Template for python3

class Solution:
    def numberOfPaths (self, M, N):
        MOD = 10**9 + 7

        def binomial_coefficient(n, k):
            result = 1
            if k > n - k:
                k = n - k  
            for i in range(k):
                result = (result * (n - i)) % MOD
                result = (result * pow(i + 1, MOD - 2, MOD)) % MOD
            return result
    
        return binomial_coefficient(M + N - 2, N - 1)
        pass
        # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        M, N = map(int, input().split())
        ans = ob.numberOfPaths(M, N)
        print(ans)




# } Driver Code Ends