# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def GetMaxlen(self,pRoot):
        if not pRoot:
            return 0
        left_len = self.GetMaxlen(pRoot.left)
        right_len = self.GetMaxlen(pRoot.right)
        max_len = max(self.Deep(pRoot.left)+self.Deep(pRoot.right), left_len, right_len)
        return max_len

    def Deep(self,pRoot):
        if not pRoot:
            return 0
        return max(self.Deep(pRoot.left),self.Deep(pRoot.right))+1
