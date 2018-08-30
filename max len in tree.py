# -*- coding:utf-8 -*-
#二叉树中最远的两结点距离
#若左右子树均存在，则最远距离为左右字数的深度和
#若只有左/右子树，则最远距离为左子树的最远距离
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
