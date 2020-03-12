# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
     例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

     分析：针对要删除重复结点的问题，我们需要记录的三个指针包括：
             当前结点前的最晚访问过的不重复结点pPre、当前结点pCur、指向当前结点后面的结点pNext

     针对结点，需要考虑的是：如果当前节点和它后面的几个结点数值相同，那么这些结点都要被剔除，然后更新pPre和pCur；
                          如果不相同，则直接更新pPre和pCur。

     这里如果 第一个结点是重复结点时，需要做下特殊处理，如果第一个结点是重复结点，那么就把头指针pHead也更新一下。

'''

def deleteduplication(phead):
    # 定义三个需要、有效的指针。   对三个指针不同场景下的操作是难点.......
    pPre=None  #用于保存 最近的之前的无重复的结点【无重复是可以保障的】、每次去重后进行更新
    pCur=phead #保存现在的结点，比较重要
    pNext=None #不断更新的，如果有后续就往后走，进行比较。

    #开始从头到尾 进行判断和考量.    当遇到后面和当前一样的重复时，进行删除操作，否则直接往后看即可。
    while pCur!=None:
        #如果跟后面的产生重复时，我们直接 删除后面的即可
        if pCur.next!=None and pCur.val==pCur.next.val:
            #这里是  考虑第一个是重复结点的处理
            pNext=pNext.next

            #  首先第一步找到合适的 pNext
            while pNext.next!= None and pNext.next.val==pCur.val:
                pNext=pNext.next
            #第二步，利用pNext  和pPre 的关系，进行一种链表方式的删除操作。用预留的 pPre 指向 非重复的目标pNext
            if pCur==phead:
                phead=phead.next
            else:
                pPre.next=pNext.next

        #当不发生重复时，继续往后走，往后看
        else:
            pPre=pCur
            pCur=pCur.next

    return phead


