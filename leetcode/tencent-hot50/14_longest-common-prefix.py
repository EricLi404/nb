# https://leetcode-cn.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                r += i[0]
            else:
                break
        return r

# if __name__ == '__main__':
