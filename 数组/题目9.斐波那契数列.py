# coding: utf-8

'''
     题目：  写一个函数，输入n，求斐波那契数列 的第 n项

     方案：  使用动态规划法，是时间复杂度非常低的方法，比较合适

'''
def fun1(n):
    res=[0,1]
    if n<2:
        return res[n]

    min1=0
    min2=1
    fib=0
    for i in range(2,n):
        fib=min1+min2
        
        min1=min2
        min2=fib
    return fib