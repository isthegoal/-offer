# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：  求单链表中的倒数第k个结点

     分析：  因为是找到倒数第 k个结点，所以需要知道对倒数位置的定位，所以一个  典型的思路。就是  不同行走任务的快慢指针。

     思路：  很经典的解法，只要设定  指针二比指针一 先走k步即可，这样当指针二走到终点，该问题就解决完毕了

'''

def last_kth(link,k):
    #先判断下  特殊情况
    if not link or k<=0:
        return None

    #  先定义移动较快的  快指针
    move=link

    #  定义快指针，这里有个问题  就会如果 链表长度小于 k的话，是有问题的，
    while move and k-1>=0:
        move=move.next
        k-=1

    if k>0:
        print('序列长度太短了')
        return None

    #开始正式的按照两个不同速度的指针进行行走吧
    while move:
        move=move.next
        link=link.next

    return link.val #ok了，不出意外，这个绝对是对的。
