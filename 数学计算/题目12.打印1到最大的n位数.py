# coding: utf-8


'''
     题目：  输入n，打印从1到最大的n位数

     方案：  这个以为python已经对大整数   进行了自动的转换，所以不需要考虑大整数溢出的问题，  就用python最简单的方法一一打印即可

'''
def pri(n):
    for i in range(10**n):
        print(i)