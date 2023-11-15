#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def betterString(self, str1, str2):
        # Code here
        a = self.countSub(str1)
        b = self.countSub(str2)

        # Return the string with more substrings
        if a < b:
            return str2
        return str1

    @staticmethod
    def countSub(str):
        # Map to store the last occurrence of characters
        last = {}

        n = len(str)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            dp[i] = 2 * dp[i - 1]

            if str[i - 1] in last:
                dp[i] = dp[i] - dp[last[str[i - 1]]]

            last[str[i - 1]] = i - 1

        return dp[n]

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str1 = input()
        str2 = input()
        ob = Solution()
        res = ob.betterString(str1, str2)
        print(res)
# } Driver Code Ends