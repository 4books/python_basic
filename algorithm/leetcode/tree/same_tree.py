# https://leetcode.com/problems/same-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.checkNode(p, q)

    def checkNode(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            # 둘다 None 인 경우
            return True
        elif p is None and q is not None:
            # 한쪽만 None 인 경우
            return False
        elif p is not None and q is None:
            return False
        elif p.val == q.val:
            # 둘다 값이 같은 경우
            leftSame = self.checkNode(p.left, q.left)
            rightSame = self.checkNode(p.right, q.right)
            if leftSame and rightSame:
                return True
            return False
        elif p.val != q.val:
            # 값이 다른 경우
            return False
