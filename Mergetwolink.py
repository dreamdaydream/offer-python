# -*- coding:utf-8 -*-
# 输入两个单调递增的链表，输出两个链表合成后的链表
# 方法1：遍历，同归并排序合并过程：p1 head p2 head 比较，小的插入，后移
# 最后比较遍历结束，p1 or p2剩下的全部插入节点就可，因为链表，只需要next指向一次就ok
# 方法2：递归
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        head = ListNode(-1)
        p = head
        while pHead1 and pHead2:
            if pHead1.val > pHead2.val:
                head.next = pHead2
                pHead2 = pHead2.next
                head = head.next
            else:
                head.next = pHead1
                pHead1 = pHead1.next
                head = head.next
        if pHead1:
            head.next = pHead1
        if pHead2:
            head.next = pHead2
        return p.next

    def Merge2(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                pHead1.next = self.Merge2(pHead1.next,pHead2)
                return pHead1
            else:
                pHead2.next = self.Merge2(pHead1,pHead2.next)
                return pHead2
