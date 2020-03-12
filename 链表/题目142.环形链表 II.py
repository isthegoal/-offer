# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
      为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
      如果 pos 是 -1，则在该链表中没有环。

          示例 1：
            输入：head = [3,2,0,-4], pos = 1
            输出：tail connects to node index 1
            解释：链表中有一个环，其尾部连接到第二个节点。

          示例 2：

            输入：head = [1], pos = -1
            输出：no cycle
            解释：链表中没有环

      分析：


     思路：快慢指针法。先判断链表有没有环，如果链表有环，则让快指针回到链表的头重新出发，当快慢指针相遇的那个节点即是
     链表环的起点。

'''

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None

        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

            if slow == fast:
                break
        if slow != fast:  # 链表无环
            return None

        fast = head
        while slow:
            if slow == fast:  # 此点即是环起点
                return slow
            slow = slow.next
            fast = fast.next
