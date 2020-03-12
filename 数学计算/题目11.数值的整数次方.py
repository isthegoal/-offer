# coding: utf-8


'''
     题目：  求一个数的整数次方

     方案：   进行计算较为简单，但是需要考虑好   次方为整数、负数、0的情况，         以及基数为0的情况。

     这里主要使用    一种思想，可以极大的减少对乘积的次数计算：
        【1】如果  exponent是偶数的话，那么  a的n次方 =  a的n/2次方  *  a的n/2次方
        【2】如果  exponent是奇数的话，那么  a的n次方 =  a-1的n/2次方  *  a-1的n/2次方  *a

     这里空间复杂度为O(1),时间复杂度为O(logn)
'''
print(12 >> 1)


#方法一.最简单的方法就是直接  使用python的 整数次方机制， 这肯定不是别人需要的
def power(base,exponent):
    return base**exponent

#第二种方法 就是利用精简化乘积的方式
#进行控制的主函数
def power(base,exponent):
    if equal_zero(base) and exponent<0:
        return '有问题，不行,0 的负数次幂 不是可行的情况'

    #开始进行   幂次计算吧        首先一次性先计算出结果
    ret=power_value(base,abs(exponent))

    #考虑负数幂情况计算
    if exponent<0:
        return 1.0/ret
    else:
        return ret

def power_value(base,exponent):
    #进行   实际的幂次计算
    if exponent==0:
        return 1
    if exponent==1:
        return base

    #现在开始对  说明处的公式进行代入。
    ret=power_value(base,exponent>>1)
    ret*=ret

    #考虑是否是奇偶的情况，这里   1对应的二进制形式是 00000001这样的....
    if exponent & 1==1:
        ret*=base

    return ret

#辅助的基数为0的情况
def equal_zero(num):
    if abs(num-0.0)<0.000001:
        return True





