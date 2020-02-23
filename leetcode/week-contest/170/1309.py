# decrypt-string-from-alphabet-to-integer-mapping 1309. 解码字母到整数映射

# 字符（'a' - 'i'）分别用（'1' - '9'）表示。
# 字符（'j' - 'z'）分别用（'10#' - '26#'）表示。
#

class Solution:
    def freqAlphabets(self, s: str) -> str:
        ss = ""
        fl = len(s) - 1
        while fl >= 0:
            if s[fl] == "#":
                ss += chr(int(s[fl - 2:fl]) + 96)
                fl -= 3
            else:
                ss += chr(int(s[fl]) + 96)
                fl -= 1
        return ss[::-1]


if __name__ == "__main__":
    s = Solution()
    ss = s.freqAlphabets("10#11#12")
    print(ss)
