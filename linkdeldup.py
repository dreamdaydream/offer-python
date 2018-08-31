# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        # 新创建result 根结点删除情况
        # res 作为result的记录节点，当不重复时直接跳到该节点，重复则next指向重复结束后的点
        result = ListNode(-1)
        result.next = pHead
        res = result
        temp = pHead
        while temp and temp.next:
            if temp.next.val == temp.val:
                #res = temp # 若重复节点保留一个
                val = temp.val
                while temp and temp.val == val:
                    temp = temp.next
                res.next = temp
            else:
                res = temp
                temp = temp.next
        return result.next

    def deleteDuplication2(self, pHead):
        # 链表转换成列表操作
        # 遍历操作需要创建新的引用
        # write code here
        value = []
        while pHead:
            value.append(pHead.val)
            pHead = pHead.next
        result = ListNode(None)
        res = result
        for i in value:
            if value.count(i) == 1:
                res.next = ListNode(i)
                res = res.next
        return result.next

    def deleteDuplication3(self, pHead):
        # 递归
        # 重复找到不重复的点开始递归
        # 不重复则next递归
        if not pHead or not pHead.next:
            return pHead
        if pHead.next.val == pHead.val:
            temp = pHead.next
            while temp and temp.val ==pHead.val:
                temp =temp.next
            return self.deleteDuplication3(temp)
        else:
            pHead.next = self.deleteDuplication3(pHead.next)
            return pHead
