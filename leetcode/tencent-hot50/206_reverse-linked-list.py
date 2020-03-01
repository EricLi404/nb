# https://leetcode-cn.com/problems/reverse-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l = l[::-1]
        root = ListNode(l[0])
        p = root
        for i in l[1:]:
            p.next = ListNode(i)
            p = p.next
        return root
