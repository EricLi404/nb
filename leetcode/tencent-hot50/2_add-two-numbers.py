# https://leetcode-cn.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1, l2, r, i1 = self.c(l1, l2, 0)
        q = r
        while l1 or l2:
            l1, l2, t, i1 = self.c(l1, l2, i1)
            q.next = t
            q = q.next
        if i1:
            q.next = ListNode(1)
        return r

    def c(self, l1, l2, i1):
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        t = ListNode((v1+v2 + i1) % 10)
        if (v1+v2 + i1) >= 10:
            i1 = 1
        else:
            i1 = 0
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        return l1, l2, t, i1


class Solution2:
    # 自己想出来的利用语法糖的写法，效率和上边那个差不多
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n = str(self.getn(l1) + self.getn(l2))[::-1]
        q = r = ListNode(int(n[0]))

        for i in n[1:]:
            t = ListNode(int(i))
            q.next = t
            q = q.next
        return r

    def getn(self, l: ListNode):
        r = ""
        while l:
            r = str(l.val) + r
            l = l.next
        return int(r)


if __name__ == '__main__':
    s = Solution()
    a = ListNode(1)
    a.next = ListNode(8)
    # a.next.next = ListNode(3)
    b = ListNode(0)
    # b.next = ListNode(5)
    # b.next.next = ListNode(6)

    c = s.addTwoNumbers(a, b)
    while c:
        print(c.val, "    |    ")
        c = c.next
