# https://leetcode-cn.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        r = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
        return r if -2 ** 31 <= r <= 2 ** 31 - 1 else 0
