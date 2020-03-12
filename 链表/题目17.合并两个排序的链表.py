# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：  合并两个排序的链表
     分析：  这里很明显  最好不应该使用外部空间，所以应该在自己本身上进行操作， 因此可以使用 递归的方法进行处理，每次先抽取出现有的有序，然后把后面的要合并的
     序列当做新的子问题，不断子问题求解网上反馈，得到整体问题的解

     思路：  构建递归， 两个只含有单链表的特殊情况。    令两个是两个链表都存在时，先感知保留一个较小值的结点，然后把后面的合并转成一个子问题去求解
'''

def merge_link(head1,head2):
    if head1 is None:
        return head2
    if not head2:
        return head1

    #比较重要的两个链表都存在时的情况  求解
    if head1.val<head2.val:
        #次数 保留head1的指向， 然后递归子问题
        ret=head1
        ret.next=merge_link(head1.next,head2)
    else:
        #考虑  head2小  或  两者相等的情况，下面处理均可
        ret=head2
        ret.next=merge_link(head1,head2.next)
    return ret
