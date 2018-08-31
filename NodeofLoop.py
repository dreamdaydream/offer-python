# -*- coding:utf-8 -*-
# 链表若成环，输出环入口
# 1 通过链表遍历，引入列表存储值，找到第一个重复值
# 2 两个指针从头A，一个指针每次走一步，一个走两步，相遇点O，快指针2x比慢指针x多走n圈环（nr）
#   快指针从头开始，慢指针相遇点开始，均一步遍历，再次相遇点即为入环点B
#   AO=AB+BO=x  OB=r-BO ==>OB=AB
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None
        value = []
        p = pHead
        while(p):
            if p in value:
                return p
            else:
                value.append(p)
            p = p.next

    def EntryNodeOfLoop2(self,pHead):
        if not pHead and pHead.next:
            return None
        p1 = pHead
        p2 = pHead
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                p2 = pHead
                while(p1!=p2):
                    p1=p1.next
                    p2=p2.next
                return p1
        return None
