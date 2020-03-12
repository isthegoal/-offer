# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
                                      如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

     分析：在这里  可以使用非常多的方式， 但是综合而言，还是 最大堆和最小堆进行结合的方案能带来的性价比最高。
             这里主要是对不同类型数据结构带来的  插入构建和  得到中位数的 时间复杂度。  时间 复杂度上的考虑

             数据结构	插入的时间复杂度	得到中位数的时间复杂度
            没有排序的数组  	O（1）	O（n）
            排序的数组	    O（n）	O（1）
            排序的链表	    O（n）	O（1）
            二叉搜索树	 【平均O（logN），最差O（n）】	【平均O（logN），最差O（n）】
            VAL树	        O（logN）	O（1）
            最大堆和最小堆	O（logN）	O（1）        每次每个插入都是logN,这样真的高效吗

     这里可以看到 VAL树的性价比也是非常高的，但是因为大部分  编程语言函数库都没有实现  这个数据结构，所以VAL具体实现不太容易。


      所以性价比 最高的还是  最大堆和最小堆的方式（最大堆是小顶堆的实现方式，最小堆是大顶堆的实现方式）。
      如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值
      使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
     （1）这里  构建 最大堆 和最小堆的思路是这样的，  针对数据流分别放入到  两个堆中，我们对堆需要满足如下性质：
                 【1】所有最大堆的数据都 大于最小堆数据
                 【2】两个堆的数据的数量差应该小于1.

       具体要如上性质时，需要针对不同情况进行考虑。
                【1】每遍历一个数据，计数器count增加1，当count是偶数时，将数据插入小根堆；当count是奇数时，将数据插入大根堆。

                    如果最大堆的堆顶数字大于最小堆堆顶数字，则把两个堆顶数字交换，重排两堆，此时两堆数字总数为偶数，取两堆堆顶数字做平均即为中位数。

                【2】当所有数据遍历插入完成后（时间复杂度为O(logn)O(logn)，如果count最后为偶数，则中位数为大根堆堆顶元素和小根堆堆顶元素和的一半；
                如果count最后为奇数，则中位数为小根堆堆顶元素。


      思路：
          使用两个堆进行实现，包括 一个大顶堆（利用相反数进行实现，之前也遇到这个问题，python的问题）、一个小顶堆
          作用：大顶堆用来存较小的数，从大到小排列；小顶堆存较大的数，从小到大的顺序排序
              这样的话，当有偶数个数据时，中位数就是小顶堆和大顶堆的堆顶元素的平均值
                       当有奇数个数据时，中位数就是大顶堆的堆顶元素


        具体实现思路（这里思路中的第一步是较为理解困难的）：
            【1】当读取数据的时候，先将数据取相反数插入大顶堆中，再将大顶堆的堆顶元素取相反数插入小顶堆中。进行完这一步操作之后，

            如果小顶堆的元素个数多于大顶堆的元素个数（即插入元素之后，所有的元素一共有奇数个）再把小顶堆的堆顶元素取相反数插入大顶堆中。
            如果小顶堆的元素个数等于大顶堆的元素个数（即当前元素的个数为偶数个），不再进行元素的变动。

            注：这里的思想特别需要解释下：  这里是为了省事，我们每次只需要把 数据放到大顶堆即可，同时为了数据均衡，把大顶堆中最大的放到小顶堆中即可。
                 这样调节很可能会不平衡，不平衡的话，就优先把多的放到大顶堆中，是这种策略吧.....

            【2】获取元素的中位数：利用小顶堆和大顶堆的元素个数来判断元素有奇数个还是偶数个（大顶堆和小顶堆的元素个数相等，偶数，
            大顶堆的元素个数多，奇数）。当有偶数个元素时，返回小顶堆和大顶堆堆顶元素的均值（别忘了大顶堆元素的负号），有奇数元素时，
            返回大顶堆的堆顶元素即可。

        在具体实现时，有两种方式吧，一种是使用python内置的堆模块，  另一种方式就是使用原生的方法自己模拟栈，其方式较为复杂一些。

'''
#使用python内部的堆利用方法
from heapq import *

class Solution:
    def __init__(self):
        #这里 使用两个结构  分别用于存储  大顶堆和小顶堆。
        self.small=[]
        self.large=[]

    #使用数据流插入数据的操作. 这里面的操作就是核心思想的体现。
    def Insert(self,num):
        small,large=self.small,self.large



        heappush(small,-heappushpop(large,-num))

        if len(large)<len(small):
            heappush(large,-heappop((small)))

    # 对构建好的插入堆结果，找到中位数的 方法
    def GetMedian(self,n=1):
        small,large=self.small,self.large

        #这个是当数据流 是奇数的情况
        if len(small)>len(large):
            return float(-large[0])

        #这个是数据流长度为 偶数的情况
        return (small[0]+large[0])/2.0



'''
    附加下， heap模块中的内置方法包括以下 函数：
heapq.heappush(heap, item)：往堆heap中插入 元素item

heapq.heappop(heap)：返回 root 节点，即 heap 中最小的元素。

heapq.heapreplace(heap,item): python3中heappushpop的更高效版。

heapq.heappushpop(heap, item)：向 heap 中加入 item 元素，并返回 heap 中最小元素。

heapq.heapify(x)：Transform list into a heap, in-place, in O(len(x)) time

heapq.merge(*iterables, key=None, reverse=False)

heapq.nlargest(n, iterable, key=None)：返回可枚举对象中的 n 个最大值，并返回一个结果集 list，key 为对该结果集的操作。

heapq.nsmallest(n, iterable, key=None)：同上相反

heapq._heappop_max(heap): Maxheap version of a heappop 

heapq._heapreplace_max(heap,item)：Maxheap version of a heappop followed by a heappush.

heapq._heapify_max(x)：Transform list into a maxheap, in-place, in O(len(x)) time

'''
