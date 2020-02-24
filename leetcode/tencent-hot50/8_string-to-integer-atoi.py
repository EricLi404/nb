# https://leetcode-cn.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, strs: str) -> int:
        strs = strs.strip().split(".")[0]
        sd = list(map(lambda x: str(x), list(range(0, 10)))) + ["+", "-"]
        if len(strs) > 0 and strs[0] in sd:
            if strs[0] == "-":
                fff = -1
            else:
                fff = 1
            if strs[0] in ["+", "-"]:
                strs = strs[1:]
            sd.remove("+")
            sd.remove("-")
            s = "0"
            for n in strs:
                if n in sd:
                    s += n
                else:
                    break
            s = fff * int(s)
            if s > 2 ** 31 - 1:
                return 2 ** 31 - 1
            if s < -2 ** 31:
                return -2 ** 31
            return s
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    a = s.myAtoi("2147483648")
    print(a)
