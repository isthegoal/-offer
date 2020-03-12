# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个链表，判断链表中是否有环。
           为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
           如果 pos 是 -1，则在该链表中没有环。

           示例 1：
            输入：head = [3,2,0,-4], pos = 1
            输出：true
            解释：链表中有一个环，其尾部连接到第二个节点。

      分析：


      思路：有两种吧。
      （1）哈希表法，线性扫描整个链表把每个访问过的节点都放进哈希表里，如果发现当前节点已经在表内，则说明链表有环。
      （2）快慢指针法。快指针一次走两步，慢指针一次走一步，如果快慢指针相遇，则说明链表有环。
'''

#哈希表法
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        record = dict()

        p = head
        while p:
            if p not in record:
                record[p] = 1
            else:
                return True
            p = p.next
        return False

#快慢指针法的方式。
def fun1(head):
    #  边界条件判别
    if not head or not head.next:
        return False

    # 创建快慢指针吧
    slow,fast=head,head

    # 进行快慢指针的行走，注意 快指针是每次走两步，慢指针每次走一步，进行判别即可。
    while fast:

        slow=slow.next
        fast=fast.next

        if fast:
            fast=fast.next
        # 进行产生重复位置的判别。核心的 如果有环，快慢指针必定会产生重叠的
        if slow==fast:
            return True

    #  如果不会碰头，那fast走完了，就没有环
    return False

