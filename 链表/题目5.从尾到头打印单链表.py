# coding: utf-8

# 题目不做解释，顾名思义

#方法一.使用 栈【列表模拟出的】，  不断将栈弹出打印
def print_links(links):
    stack=[]
    while links:
        stack.append(links.val)
        links=links.next

    #这个是后进先出吧
    while stack:
        print(stack.pop())


#方法二.使用直接递归的方法    ,递归不断进行打印
def print_link_recursion(links):
    if links:
        #递归，通过控制递归语句的位置，可以有效的控制是  头打印， 还是尾打印
        print_link_recursion(links.next)
        print(links.val)

