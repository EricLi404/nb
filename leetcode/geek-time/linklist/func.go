package linklist

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func GetOneListNode(ii []int) *ListNode {
	p := &ListNode{
		Val:  ii[0],
		Next: nil,
	}
	f := p
	for i := 1; i < len(ii); i++ {
		f.Next = &ListNode{
			Val:  ii[i],
			Next: nil,
		}
		f = f.Next
	}
	return p
}

func Display(l *ListNode) {
	for l != nil {
		fmt.Println(l.Val)
		l = l.Next
	}
}
