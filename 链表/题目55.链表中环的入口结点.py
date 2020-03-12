# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：一个链表中包含环，请找出该链表的环的入口结点。


     分析：这个是非常传统的思路，就是 一个走两步，一个走一步，先碰头后，再继续走的问题。

     (1)这里为什么要这样走的原因，其实不太好明白，主要是进行获取环中有多少个结点。https://cuijiahua.com/blog/2018/01/basis_55.html

     原因：
     如果知道环中的结点数n，那么  P1先走n步，那么这样继续走后，P1和P2肯定会在入口地方碰头，这是因为P2比P1落后
     可是一个n,那么就是P1先走，因为其是先走了n，那么我们以 环入口来看，P2走到环入口 时，P1因为环性质肯定会循环到环入口，因为P1先于一个n走到环入口，那么当一个n
     后P2到达环入口时，P1必定会再循环到环入口。

     因此这里有个核心是怎么知道环中有多少结点，这个是解法的关键 ！


     这里使用双指针的思路，步骤是如下的思想：
     【1】先定义 P1和P2两个指针指向链表的头结点，这两个指针称之为快慢指针，一个每次走一步，一个每次走两步。
     这样行走后，如果两个指针相遇，说明链表中存在环，且相遇的位置在环中。
     【2】之后从相遇的环中结点继续出发， 一遍继续走 一遍 移动步数，当重新回归到 原来的相遇点时，此时计数值就是环中结点数目。
     【3】知道环中结点数目中，再一波双指针行走即可，一个先走k，另一个从起始处开始，一块走到碰头...。

     (2)上面的方法好麻烦，但是也是比较直观好解释，  同时可以获得环中数量和 环入点两个信息。
     另一个是之前看到的....

'''


class solution:
    #大的主函数
    def EntryNodeofloop(self,phead):
        if phead==None:
            return

        # 使用一个函数来获取得到 第一步中 两个指针会相遇的结点meetingn，一定要存在
        meetingn=self.meetingnode(phead)
        if meetingn==None:
            return None

        #第二步，根据相遇的位置，开始计算统计循环的次数nodesloop
        nodesloop=1
        node1=meetingn

        while node1.next!=meetingn:
            node1=node1.next
            nodesloop+=1

        #第三步吧，一个先走nodesloop步，另一个再开始，最后再聚首,聚首位置返回node1就行。
        node1=phead
        for _ in range(nodesloop):
            node1=node1.next
        node2=phead
        while node1!=node2:
            node1=node1.next
            node2=node2.next

        return node1

    #对  链表 寻找到   初始第一个 相遇的位置点
    def meetingnode(self,phead):
        #首先定义快慢指针
        slow=phead.next
        if slow==None:
            return None
        fast=slow.next

        #对 快慢指针不断往后走，但只这里注意，fast是多走了一步，每次走两步
        while fast!=None and slow!=None:
            if slow==fast:
                return fast

            #快慢指针的挪动
            slow=slow.next
            fast=fast.next
            if fast!=None:#这个判断很有必要，是考虑闭环的情况，如果下一个为空，就会闭环呗。
                fast=fast.next

        return None
