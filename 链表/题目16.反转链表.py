# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：  对链表进行直接的翻转

     分析：  该问题之前遇到过，最为好的方法，应该是每次都在本身上进行翻转，  而不占据任何空间复杂度

     思路：  维持 三个指针，分别是
             【1】head指针：指向新的逆序链表的尾部
             【2】then指针：指向原链表现有的第一个，  用于第一个被逆过去
             【3】last指针，指向原链表现有的第一个的后一个，用于  更新新的then
             在本身的空间复杂度上，就行了，很方便的思想。

'''
def reverse_link(head):
    #先考虑空链表的情况
    if not head or not head.next:
        return head

    #现在考虑  新的  逆序的放在head上，   原来的顺序用last和then保存
    then=head.next
    head.next=None
    last=then.next

    while then:
        #注意看清楚这三行，让  then指向原来的head，同时   保持last和then新的指向。  始终让   head指向新的尾部，让then指向原序列的首个，then指向下一个。这三个位置各司其职
        then.next=head
        head=then
        then=last

        #更新last始终位于后一个，用于每次更新时位于   原序的第一个，  因为前一个已经跟着逆序的跑了
        if then:
            last=then.next

        return head