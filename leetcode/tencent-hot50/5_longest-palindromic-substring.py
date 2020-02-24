# https://leetcode-cn.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        ml = 0
        sts = 0
        dp = [[False for _ in range(size)] for _ in range(size)]
        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j]:
                    if j - i > ml:
                        ml = j - i
                        sts = i
        return s[sts:sts + ml + 1]


if __name__ == '__main__':
    s = Solution()
    a = s.longestPalindrome("vabaiabca")
    print(a)
