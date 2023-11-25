class Solution:
    def shuffleArray(self, arr, n):
        # Your code goes here
        n = len(a)
        k = n // 2 - 1

        for i in range(n - 1, n // 2 - 1, -1):
            a[i] <<= 10
            a[i] |= a[k]
            k -= 1

        k = 0

        for i in range(n // 2, n):
            a[k] = a[i] & 1023
            k += 1
            a[k] = a[i] >> 10
            k += 1

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a = list(map(int,input().split()))
        ob = Solution()
        ob.shuffleArray(a,n)
        print(*a)
# } Driver Code Ends