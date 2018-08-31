# -*- coding:utf-8 -*-
# 返回从尾部到头部的列表值序列，例如[1,2,3]
# 方法1：遍历链表存list,翻转输出，注意翻转的几种方法
# 方法2：遍历，通过insert（0，val）不反转
# 方法3：递归，从后往前递归
# 还可以通过栈 入栈pop出栈翻转，python 没有栈，可通过list，append，pop 需要两个列表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    
    def printListFromTailToHead(self, Head):
        result = []
        if not Head:
            return []
        while Head:
            result.append(Head.val)
            Head = Head.next
        #return list(reversed(result))
        return result[::-1]

    def printListFromTailToHead2(self, Head):
        result = []
        if not Head:
            return []
        while Head:
            result.insert(0, Head.val)
            Head = Head.next
        return result

    def printListFromTailToHead3(self, Head):
        result = []
        if not Head:
            return []
        if Head:
            result = self.printListFromTailToHead(Head.next)
            result.append(Head.val)
        return result
