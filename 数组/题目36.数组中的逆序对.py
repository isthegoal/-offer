# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：在一个数组中，前面的数字比后面的大，就是一个逆序对，求总数
           （求数组中逆序 序列的数量）

           例如在数组｛7, 5, 6, 4 }中， 一共存在5 个逆序对，分别是（7, 6）、（7，5），(7, 4）、（6, 4）和（5, 4）

     分析：   首先逐步思考，
             （1）从最简单的方式思考的话，第一种方法是直接求解法。
                  顺序扫描数组，每扫描到一个数字，就逐个比较该数字和它后面的数字的大小，如果后面的数字小于前面的数，直接累计计数就行了

             （2）第二种就是面试官想要的  二分的一种思想，其实讲道理就会重新进行一次归并排序，只不过排序过程中进行逆序次数上的统计。
                    主要参考讲解：https://cuijiahua.com/blog/2018/01/basis_35.html
                    *将长度为n的数组，不断进行分解，分离成n/2、n/2/2、这样不断细化的过程（回顾下归并排序的思想就是这样，先很细的进行合并）
                    *在每个细化部分，进行统计和排序，此时逆序对总数= 左边数组中逆序对数量+右边数组逆序对数量+左右结合成新的顺序数组中逆序对数量。
                       【1】首先 分开的左或者右边逆序对统计，在递归中一般是 我们都会按照左右结合的思想进行二分，比如长度只有两个时，可以看做
                       左数组长度为1，右数组长度为1的合并。
                       【2】核心的常规的主要用的  对左右序列进行结合的思想。进行结合时候有三个点需要注意，一个是 需要考虑三种情况[大小值比较上的三种]。
                        另一个是进行左右两部分比较时一定要设置两个指针分别从各自后往前找，当发现找到左边的都大于右边的，则右边的长度就是逆序的统计长度
                        最后一个是在归并过程中，统计过后，避免再次统计，一定要记得进行排序，按从小到大对每个子部分进行排序。

     思路：
'''
import copy
def get_inverse_pair(nums):
    #主函数部分，在该部门启动整个的二分和统计
    if not nums:
        return 0

    start,end=0,len(nums)-1
    temp=copy.deepcopy(nums)
    return inverse_pairs(temp,start,end)

def inverse_pairs(tmp,start,end):
    #二分递归截止      不断二分递归所必须的截止条件
    if start==end:
        return 0

    # 折半方式的  分别对左右两边递归求值....    这里我们会按照归并的思想，先分成小的，再不断排序合并的过程
    mid=(end-start)/2
    left=inverse_pairs(tmp,start,start+mid)
    right=inverse_pairs(tmp,start+mid+1,end)

    # 针对本次逆序求数目，做统计       最为重要的地方，  双指针下的遍历及统计
    count=0
    #首先定位到  两个序列的尾部
    l_right,r_right=start+mid,end
    t=[]
    #第一波，针对  两个序列的尾部，进行数值的比较来考虑指针向前挪动。           并在统计count计数时，把排序好的数组保存到 t 序列中去。
    while l_right >=start and r_right>start+mid+1:
        if tmp[l_right]>tmp[r_right]:
            t.append(tmp[l_right])
            count+=(r_right-mid-start)
            l_right-=1
        else:
            t.append(tmp[r_right])
            r_right-=1

    #第二波，是在第一波之后，发现 有一个数组已经走完之后，那么剩下的数组  就是最大的  那几个数字， 直接拼到后面就行了
    while l_right>=start:
        t.append(tmp[l_right])
        l_right-=1
    while r_right>=start+mid+1:
        t.append(tmp[r_right])
        r_right-=1

    #最后的统计和返回。    切记这里的tmp就类似全局变量一样，是不断被改变的。      算是    简单的递归  归并排序的思想吧
    tmp[start:end+1]=t[::-1]#   归并排序的结果产生效果的地方，  之后的归并会基于该排序后的效果再做统计。

    return count+left+right



