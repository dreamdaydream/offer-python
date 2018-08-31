# -*- coding:utf-8 -*-
# 链表的第一个公共节点：单链表，若有相同的节点，node.next 则后面节点均相同，Y型
# 方法1：若有公共节点，长度相同的两链表，从第一个相同的节点开始同时到达尾节点，长链表先走长度差。O(m+n)
# 方法2：链表转换列表操作，只有在列表中有值，则为相同节点 O(m+n)
# 方法3：为了遍历长度相同节点，p1 == Null ? p2,p1.next
# {1,2,3,4,5}{6,7,4,5}==>
# {1,2,3,4,5,6,7,4,5}
# {6,7,4,5,1,2,3,4,5}
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        def getlistlength(pHead):
            length = 0
            while pHead:
                length += 1
                pHead = pHead.next
            return length

        def jumpnode(pHead, l):
            for i in range(l):
                pHead = pHead.next
            return pHead

        len1 = getlistlength(pHead1)
        len2 = getlistlength(pHead2)
        if len1 > len2:
            pHead1 = jumpnode(pHead1, len1 - len2)
        else:
            pHead2 = jumpnode(pHead2, len2 - len1)
        while pHead1 and pHead2:
            if pHead1.val == pHead2.val:
                return pHead1
            else:
                pHead1 = pHead1.next
                pHead2 = pHead2.next
        return None

    def FindFirstCommonNode2(self, pHead1, pHead2):
        list1 = []
        while pHead1:
            list1.append(pHead1.val)
            pHead1 = pHead1.next
        while pHead2:
            if pHead2.val in list1:
                return pHead2
            else:
                pHead2 =pHead2.next
        return None

    def FindFirstCommonNode3(self, pHead1, pHead2):
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            p1 = p1.next if p1 else pHead2
            p2 = p2.next if p2 else pHead1
        return p1




