# https://leetcode-cn.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        dp_table = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(len1 + 1):
            dp_table[i][0] = i
        for j in range(len2 + 1):
            dp_table[0][j] = j
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if word1[i - 1] == word2[j - 1]:
                    dp_table[i][j] = dp_table[i - 1][j - 1]
                else:
                    dp_table[i][j] = min(dp_table[i - 1][j - 1], dp_table[i - 1][j], dp_table[i][j - 1]) + 1
        return dp_table[-1][-1]

    def p(self, l):
        for i in l:
            print(i)


if __name__ == '__main__':
    s = Solution()
    a = s.minDistance("horse", "ros")
    print(a)
