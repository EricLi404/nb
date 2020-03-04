from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def dfs(n: TreeNode, depth):
            if not n:
                return
            if len(r) == depth:
                r.append(n.val)
            dfs(n.right, depth + 1)
            dfs(n.left, depth + 1)

        r = []
        dfs(root, 0)
        return r


if __name__ == '__main__':
    # [1, 2, 3, null, 5, null, 4]
    # [1, 2, 3, 4]
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    # p.right.right = TreeNode(4)
    p.left.left = TreeNode(4)
    s = Solution()
    o = s.rightSideView(p)
    print(o)
