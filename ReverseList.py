# -*- coding:utf-8 -*-
# 方法1，三个指针遍历
# 方法2，pHead.next 尾节点 递归每次都是在尾节点插入
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pre = None
        if not pHead or not pHead.next:
            return pHead
        while pHead:
            # pre pHead pnext
            pnext = pHead.next  # pnext 保存下一个节点指针
            pHead.next = pre    # 反转指针
            pre = pHead         # 指针前移 遍历
            pHead = pnext
        return pre

    def ReverseList2(self,pHead):
        if not pHead or not pHead.next:
            return pHead
        reversehead = self.ReverseList2(pHead.next)
        pHead.next.next =pHead
        pHead.next = None
        return reversehead
