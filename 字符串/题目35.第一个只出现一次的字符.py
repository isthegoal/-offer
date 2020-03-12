# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
     题目：   求字符串中第一个只出现一次的字符

     分析：   很简单的思路，这种由统计次数的，最简单的方法就是  hash表，这里打算使用两个hash表。
              第一个hash表用于记录每个字符出现的次数，另一个哈希用于记录字符第一次出现的索引位置。
     思路：    思路如上，简单实现即可

'''

def fun1(string):
    #首先  永远是思考边界条件
    if string==None:
        return -1

    #创建两个字典吧    计数字典 和 首索引字典
    count={}
    loc={}

    #为了获得索引，这里使用下迭代器吧
    for k,s in enumerate(string):
        #字典的get方法也得非常熟练下
        if count.get(s):
            count[s]=count[s]+1
        else:
            count[s]=1

        if loc.get(s):
            loc[s]=loc[s]
        else:
            loc[s]=k

    #上面  字典创建完成后，下面就可以去看字典成果了
    ret=float('inf')#最大索引变量    把两个查找合在一起
    for k in loc.keys():
        #双重条件得到最小索引
        if count['k']==1 and loc[k]<ret:
            ret=loc[k]

    return ret