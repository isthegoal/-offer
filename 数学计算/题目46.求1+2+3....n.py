# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精
from functools import reduce
'''
     题目：  特简单，计算  1+2+3....的累加和
              不能使用乘除、for、while、if、else等操作
     分析：  无敌送分题吧，使用range和sum组合即可

                         第二种方法是使用reduce


'''
#第一种极其简单的方法
def get_sum1(n):
    return sum(range(1,n))

#第二种  是使用reduce关键字的方式。      reduce() 函数会对参数序列中元素进行累积
#这是整个函数的性质吧，  就这样吧，这个解法没多大意义。
def get_sum2(n):
    return reduce(lambda x,y:x+y ,range(1,n+1))

'''
     题目：    把47也一起说一下，基本不会考，  不用加减乘除做 加法
              
     分析：  


'''
def add1(n1,n2):
    return sum([n1,n2])


