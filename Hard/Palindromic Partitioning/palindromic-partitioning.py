#User function Template for python3

class Solution:
    def palindromicPartition(self, string):
        # code here
        n = len(string)

        # Initialize a 2D table to store if substrings are palindromes
        is_palindrome = [[False] * n for _ in range(n)]
    
        # Initialize the cuts array to store minimum cuts required
        cuts = [0] * n
    
        for i in range(n):
            min_cuts = i
            for j in range(i, -1, -1):
                if string[i] == string[j] and (i - j < 2 or is_palindrome[j + 1][i - 1]):
                    is_palindrome[j][i] = True
                    if j > 0:
                        min_cuts = min(min_cuts, cuts[j - 1] + 1)
                    else:
                        min_cuts = 0
                else:
                    is_palindrome[j][i] = False
            cuts[i] = min_cuts
    
        return cuts[n - 1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends