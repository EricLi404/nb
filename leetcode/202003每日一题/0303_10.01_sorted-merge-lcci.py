# https://leetcode-cn.com/problems/sorted-merge-lcci/
from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        a_tail = m + n - 1
        a_flag = m - 1

        for i in B[::-1]:
            while a_flag >= 0 and i < A[a_flag]:
                A[a_tail] = A[a_flag]
                a_tail -= 1
                a_flag -= 1
            A[a_tail] = i
            a_tail -= 1
        print(A)


if __name__ == '__main__':
    s = Solution()
    # [2, 0]
    # 1
    # [1]
    # 1
    s.merge([2, 0], 1, [1], 1)
