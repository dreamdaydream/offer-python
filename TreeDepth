# -*- coding:utf-8 -*-
#树的深度，根节点为1
#TreeDepth为递归方法，左右节点递归的最大值
#2为非递归遍历法，层次遍历，d++
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self,root):
        if not root:
            return 0
        return max(self.TreeDepth(root.left),self.TreeDepth(root.right)) + 1

    def TreeDepth2(self,root):
        if not root:
            return 0
        temp = [root]
        d = 0
        while temp:
            for i in range(0, len(temp)):
                t = temp.pop(0)
                if t.left:
                    temp.append(t.left)
                if t.right:
                    temp.append(t.right)
            d +=1
        return d
