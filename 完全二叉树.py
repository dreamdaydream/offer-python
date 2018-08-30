# -*- coding:utf-8 -*-
# 完全二叉树，空节点之后无有效节点
# 层次遍历，设置标志位status=False，遇到空节点，设置为True,当遇到下一个有效节点值，则说明非完全二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def IsComplete(self, pRoot):
        if not pRoot:
            return True
        #result = []
        status = False
        temp = [pRoot]
        while temp:
            t = temp.pop(0)
            if t:
                #result.append(t.val)
                if status:
                    return False
                temp.append(t.left)
                temp.append(t.right)
            else:
                status = True
        return status
