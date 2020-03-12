# coding: utf-8

'''
    要求 ：  用两个栈实现队列，分别实现入队和出队操作 思路：一个栈负责入队，另一个负责出队，出栈为空则从入栈中导入到出栈中

    思路：需要实现队列核心的 先入先出的操作，  就需要两个栈联合进行合作
           栈1用于直接存放，栈2完全是为了配合来直接弹出的先弹完  栈2.

'''

class queue():
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self,val):
        #将数据压到队列尾部， 就是放入栈中
        self.stack1.append(val)


    def pop(self):
        # 将stack2中的信息弹出来，      stack2反正就是用来弹出的。   【先进后出的弹pop】
        if self.stack2:
            return self.stack2.pop()
        #将stack1中的信息  不断弹当到2中
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            return '空'