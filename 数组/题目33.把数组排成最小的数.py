# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
     题目：   把数组中的值拼接，找出能产生的最小的数[321,32,3]，能够拼接出的最小的数是321323

     分析：

     思路：  这个题的做法很巧妙，把要比较的两个数字进行不同顺序的前后拼接，进行大小比较。剑指Offer上有个证明，
             证明了按拼接次序进行排序得到的数字串变成str后数字是最小的。


                遇到这个题，全排列当然可以做，但是时间复杂度为O(n!)。在这里我们自己定义一个规则，对拼接后的字符串进行比较。
                排序规则如下：
                若ab > ba 则 a 大于 b，
                若ab < ba 则 a 小于 b，
                若ab = ba 则 a 等于 b；
                根据上述规则，我们需要先将数字转换成字符串再进行比较，因为需要串起来进行比较。比较完之后，按顺序输出即可。


                好吧，明白了，按照这个排序规则
                那么[321,21,3]  经过排序后就是 ['21', '321', '3']  。 从而得到了213213 。  好吧，巧妙在这里，是定了一个顺序了

'''


#  这里主要对  python语法的利用比较精妙一些吧;
'''
      参考这里的一处说明：https://blog.csdn.net/zhu_lydia/article/details/86472647
    
      sorted(cmp=)   :  返回一个经过排序的列表,cmp是自己定义的比较函数
      
       这里就是按照自己的规则来比较排序

'''
from functools import cmp_to_key

def cmp1(a,b):
    return int(str(a)+str(b)) - int(str(b)+str(a))

#是按照自己独特的排序规则成功的，牛逼的方式
def print_mini(nums):
    return  int(''.join([str(num) for num in sorted(nums, key=cmp_to_key(cmp1))]))

print([str(num) for num in sorted([321,21,3], key=cmp_to_key(cmp1))])


print(print_mini([321,21,3]))