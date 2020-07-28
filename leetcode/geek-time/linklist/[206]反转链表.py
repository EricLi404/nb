# 反转一个单链表。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL 
# 
#  进阶: 
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？ 
#  Related Topics 链表 
#  👍 1112 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.

from .func import ListNode, arr2linklist, iterate_linklist


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = ListNode(0)
        p = pre
        h = head
        while head.next is not None:
            h.next = p.next
            p.next = h
        return pre.next


if __name__ == '__main__':
    l = arr2linklist([1, 2, 3, 4])
    iterate_linklist(l)
    s = Solution()
    ll = s.reverseList(l)
    iterate_linklist(ll)
