class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        maxlen = 1
        start = 0
        
        # Size 1
        for i in range(0, len(s)):
            dp[i][i] = 1
            
        # Size 2
        for i in range(0, len(s) - 1):
            if(s[i] == s[i + 1]):
                dp[i][i+1] = 1
                maxlen = 2
                start = i
        
        # Size 3 to n
        for k in range(3, len(s)+1):
            for i in range(0, len(s) - k + 1):
                j = i + k - 1
                
                if (dp[i+1][j-1] == 1 and s[i] == s[j]):
                    dp[i][j] = 1
                    if (k > maxlen):
                        maxlen = k
                        start = i
        
        return s[start:start+maxlen]
                    