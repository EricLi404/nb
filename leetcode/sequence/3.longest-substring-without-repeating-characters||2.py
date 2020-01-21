class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m, i, j = 0, 0, 0
        s += " "
        while j < len(s) - 1:
            j += 1
            m = max(j - i, m)
            i += (1 + s[i:j].find(s[j]))
        return m


if __name__ == '__main__':
    ss = Solution()
    r = ss.lengthOfLongestSubstring("pwwkew")
    print(r)
