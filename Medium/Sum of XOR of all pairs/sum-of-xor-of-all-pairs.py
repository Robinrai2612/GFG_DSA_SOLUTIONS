#User function Template for python3

class Solution:
    def sumXOR (self, arr, n) : 
        sum = 0
        for i in range(32):
            oneCnt = 0
            zeroCnt = 0
            for j in range(n):
                if arr[j] % 2 == 0:
                    zeroCnt += 1
                else:
                    oneCnt += 1

                arr[j] //= 2
            
            sum += (zeroCnt * oneCnt) * (1 << i)
        return sum



#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.sumXOR(arr, n)
    print(res)


# } Driver Code Ends