class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        for i in range(len(s)):
            stt = str(s[i])
            for k in s[i + 1:]:
                if k not in stt:
                    stt += str(k)
                else:
                    break
            if len(stt) > l:
                l = len(stt)
        return l

# 还可以用滑动窗口做


if __name__ == '__main__':
    ss = Solution()
    r = ss.lengthOfLongestSubstring("aab")
    print(r)
