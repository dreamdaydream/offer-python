# -*- coding:utf-8 -*-
# 方法1：链表转换list操作，切片[-k]
# 方法2，3：两个指针，一个P1指向正数第k,一个p2头节点，同时遍历，p1到达尾部时，p2到达倒数第k个
# ps: 方法2是利用range 移动k-1次 3是count计数，比较为k 因为最后输出p1为None,p2为倒数第k
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k ==0:
            return None
        value = []
        while head:
            value.append(head)
            head = head.next
        return value[-k] if k<=len(value) else None

    def FindKthToTail2(self, head, k):
        # write code here
        if not head or k == 0:
            return None
        p1 = head
        p2 = head
        for i in range(k - 1):
            if p1.next:
                p1 = p1.next
            else:
                return None
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        return p2

    def FindKthToTail3(self, head, k):
        # write code here
        if not head or k == 0:
            return None
        p1=head
        p2=head
        count = 0
        while p1:
            if count>= k:
                p2 = p2.next
            p1 =p1.next
            count +=1
        return p2 if count>=k else None
