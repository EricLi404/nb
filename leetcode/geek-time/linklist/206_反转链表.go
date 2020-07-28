//反转一个单链表。
//
// 示例:
//
// 输入: 1->2->3->4->5->NULL
//输出: 5->4->3->2->1->NULL
//
// 进阶:
//你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
// Related Topics 链表
// 👍 1125 👎 0

//leetcode submit region begin(Prohibit modification and deletion)

package linklist

func reverseList(head *ListNode) *ListNode {
	pre := ListNode{
		Val:  0,
		Next: nil,
	}

	for head != nil {
		m := pre
		t := ListNode{
			Val:  head.Val,
			Next: &m,
		}
		pre.Next = &t
		head = head.Next
	}
	return pre.Next
}
