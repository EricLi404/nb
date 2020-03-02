# https://leetcode-cn.com/problems/merge-two-sorted-lists/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        lll = self.gl(l1) + self.gl(l2)
        lll.sort()
        if len(lll) == 0:
            return l1
        root = ListNode(lll[0])
        p = root
        for i in lll[1:]:
            p.next = ListNode(i)
            p = p.next
        return root

    def gl(self, l):
        ll = []
        while l:
            ll.append(l.val)
            l = l.next
        return ll


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = ListNode(0)
        q = p
        while l1 and l2:
            if l1.val < l2.val:
                q.next = l1
                l1 = l1.next
            else:
                q.next = l2
                l2 = l2.next
            q = q.next
        q.next = l1 if l2 is None else l2
        return p.next
