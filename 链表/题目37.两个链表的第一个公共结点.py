# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：输入两个链表，找出它们的第一个公共结点。
                     其形式 是这样的，什么叫做有公共结点呢，   链表1：      a1  a2  c1   c2   c3
                                                            链表2:  b1  b2  b3  c1    c2  c3   【就是这种后面几个相同的形式】

     分析： 首先这里肯定需要逐个遍历，而且需要配合链表本身的性质，只能从前往后遍历，而不能从后往前遍历。

           感觉思路的话，可以有多种方式：
              【1】首先获取链表1和链表2的长度，之后让长的链表先走 长度差值步数。   之后就可以让链表1和链表2同时走了
               在行走时，当发现走到一定步数后两个链表后面的指向都相当，则说明到了  公共结点处

               假定一个长L1,一个长L2,则时间复杂度是O(L1+L2).   空间复杂度是O(MAX(m,n))


              【2】就上面的就够了


'''
def fun1(link1,link2):
    #首先边缘判断
    if not link1 and not link2:
        return None

    #接下来分别获取两个链表的长度
    length1=length2=0
    move1,move2=link1,link2 #定义移动用的指针，不能在本身上去移动

    while move1:
        length1+=1
        move1=move1.next

    while move2:
        length2+=1
        move2=move2.next

    # 让更长的指针先走一段距离
    while length1>length2:
        length1-=1
        link1=link1.next

    while length2>length1:
        length2-=1
        link2=link2.next

    #开始最后的核心部分，在移动后，让两个链表同时行走吧  . 当发现是公共结点时，就返回。这里的link1==link2是链表指向方式的比较， 比较了很多东西
    while link1:
        if link1==link2:
            return link1
        link1,link2=link1.next,link2.next

    return None




