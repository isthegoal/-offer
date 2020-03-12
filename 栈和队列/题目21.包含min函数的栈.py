# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：  定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数

     分析：  看来这里的意思，是首先是必须维护和实现一个栈，  同时我们能够随时打印出栈的最小值。

            这里的基本思想是使用一个  辅助的栈  来专门存储最小值，  并且保持 辅助栈的最后一个数肯定存储的是最小值。
                此时主要就牵扯到出栈  和 入栈 两个操作
                 【1】出栈：伴随着原栈的弹出，  辅助栈也弹出最后一个
                 【2】入栈：这里的入栈操作是核心，也是最为有技巧性的，入栈时 新的数小于 原来的最后一位数，那就当成最小的放进栈即可，
                      如果 新进的数大于之前的最后一个，说明现在这个肯定不是最小的，方法就是把原来的最后一个复制下，从而保持最后一个永远是整个序列最小的

     思路：  就按照如上操作吧，  主要实现三个函数，从两个栈本身的意义出发， 实现栈的更新与调整。

'''
class Mystack():
    def __init__(self):
        self.stack=[]  #栈和队列 都是用列表实现，只是控制好 出来时的位置。
        self.min=[]

    def push(self,val):
        # 正常栈的操作
        self.stack.append(val)

        #对min栈的  压栈操作， 要考虑之前思考的那个问题，始终保持最后一个最小
        if self.min and self.min[-1]<val:
            self.min.append(val)
        else:
            self.min.append(min[-1])

    def pop(self):

        #这里必须得  min栈伴随着  普通栈的弹出，弹出最后一位数
        if self.stack:
            self.min.pop()
            return self.stack.pop()
        return None

    #弹出最小值的  操作，非常简单
    def min(self):
        return self.min[-1] if self.min else None
