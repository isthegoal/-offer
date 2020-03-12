# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
     题目：从扑克牌中随机抽取5张牌，判断是不是顺子，大小王可以当任意值(这里有个非常重要的条件，大小王是任意值)

     分析： 当被判定为顺子时，需要满足四个条件（顺子肯定是  按照有序的，逐个增加的形式）：
          【1】输入的数据个数为5
          【2】输入数据在0-13之间
          【3】没有相同的数字
          【4】最大值和最小值之间的差值 不大于5
          【附加】特别的针对大小王的思考，如果是大小王，直接continue不管这一条件即可

          这里  最大最小差值不大于5，其实就是  对逐步单个递增上的约束，满足这四个条件就是极大的直接的 约束，而且不需要使用排序的方法。
          这里主要有两种思路吧：
          【1】先进行排序，后统计的思路。  统计逐步递增的情况,但是这里有个难点是对大小王的利用
          【2】直接不进行排序， 这样可以避免排序本身所带来的时间复杂度，使用 上面的四点的限制的即可。
'''




#   使用不 排序的思路      这里传过来的就是随机数numbers
def iscontanis(numbers):
    #第一条件判别
    if len(numbers)<5:
        return False

    #外部 统计最大最小的情况
    min_num=-1
    max_num=14
    flag=0#为第三判别条件服务

    for number in numbers:
        #第二判别条件
        if number<0 and number>13:
            return False

        # 有些难以理解的 第三判别条件。     下面的判别条件中，用于判别过去存在过，产生重复了，这个很核心的，但是
        # 这里标准操作// 如果数字已经出现了一次  if (flag>>number) & 1 ==1
        #但是  这里为什么下面三行可以 起到判别 在过往中出现一次的效果。    在于二进制上的进位操作吧
        '''
           此处其实有点小绕， 但是可算是想明白了，这里  主要是 靠 flag上的位来保存过往出现的数值。
              
           核心的秘密就在于   flag>>number 上，我们实际上是将数字保存在flag的位数上了。通过flag就可以
           保存过去所有的情况。 比如我们保存过去的数字3时，就可以映射到二进制位数flag中的1000
                                                      同理5映射成二进制中的100000
                                                      
           这样使用位数存储的方式，就可以极其有效的 简化对内存空间的占用，使用O(1)的空间复杂度即可，真的是流弊的方法
            
        '''
        #此处  是 判断flag二进制精简哈希中，  对应的num位数上是否已经存在过
        if (flag>>number) & 1 ==1:
            return False
        #对应将  当前数字存储到flag二进制精简哈希中，注意这里是   把flag与其合并了。
        flag |= 1 << number

        # 对大小王这种bug的处理，直接  当做一个特别的数字，  contiue即可
        if number==0:
            continue

        #第四判别条件的判定
        if number<min_num:
            min_num=number
        if number>max_num:
            max_num=number
        if max_num-min_num>=5:
            return False
    #最后 如果通过了false的考验，true即可
    return True

#iscontanis([3,4,0,6,7])




#使用排序的方式  就较为简单些。   【不简单， 这里很大的问题是 】
#这里的方式  是给出大的集合先排序  后 进行判别吧
import random
def iscontanins2(nums,k):
    #首先从 nums中   获取  随机的k个数
    data=[random.choice(nums) for _ in range(k)]

    #内在方式  直接排序
    data.sort()

    #找到大王小王的索引位置， 其实也就获得了 可以变换成任意牌的大小王牌数量    zero含义是大小王牌的数量
    zero=data.count(0)
    #根据排序后的0值开始，进行往后的行走遍历    small,big含义是当前走的前后两个相差一索引
    small,big=zero,zero+1

    #开始从前往后 的探索，   切记这里非常大的难点是对 大小王牌的利用

    # 共k张牌，遍历所有 主要要考虑的牌
    while big<k:

        # 第一种情况，如果存在 重复的牌，当然就有问题，大小王不会在此存在
        if data[small]==data[big]:
            return False

        #前一个和后一个之间的 差距， 这种差距如果大于1，主要是可以靠  大小王牌进行补充【这是这里的一个小难点】
        tmp=data[big]-data[small]

        #如果需要大小王进行补充时
        if tmp>1:
            #当使用大小王无法补充时
            if tmp-1>zero:
                return False
            else:
                #如果使用大小王可以补充    就进行补充吧。  进行补充后对可用大小王个数进行更新
                zero-=tmp-1
                small+=1
                big+=1
        #不需要补充时，直接往后走
        else:
            small+=1
            big+=1

    return True












