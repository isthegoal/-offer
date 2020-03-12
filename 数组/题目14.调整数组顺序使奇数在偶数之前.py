# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：  对于一个数组，调整顺序，使得数组顺序中奇数位于偶数前面

     分析： 这道题还是比较简单，直接使用快速排序中的pardition函数的思想即可，双指针进行搜索使得在最终 位置点左侧都是奇数，右侧都是偶数。

'''
def reorder(nums):
    #设定指针初始位置
    left,right=0,len(nums)-1

    while(left<right):
        while not is_even(nums[left]):
            left+=1
        while is_even(nums[right]):
            right-=1
        if left<right:
            nums[left],nums[right]=nums[right],nums[left]

def is_even(num):
    #直接判断是否是偶数的函数，贼简单的位比较即可
    return (num&1)==0