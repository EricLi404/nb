class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def arr2linklist(arr):
    root = ListNode(arr.pop(0))
    p = root
    for i in arr:
        p.next = ListNode(i)
        p = p.next
    return root


def iterate_linklist(head):
    print(head.val)
    while head.next is not None:
        head = head.next
        print(head.val)
