# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,

      分析：这题感觉还是有多种思路的
              【1】全部升序排序， 然后输出 前k个数， 这个方法就是使用快速排序，时间复杂度是  O(nlogn)
              【2】使用快排中的partiton函数，利用该函数的性质，因此如果排序之后枢轴刚好处于数组的第k个位置，那么此时数组的前k个数字也即是最小的k个数。
              这种方法经过算法导论树书中证明，时间复杂度是O(n)

              ①我们设定partition函数的哨兵为key=lists[left]，在partition函数中完成一轮比较的结果是，比key大的数都在其右边，比key小的数放在其左边。
              完成该轮后返回其left=right时left的值。

              ②我们判断left的值是比k大还是小：如果left的值比k大，说明上轮partition之后，lists中前left个小的数在左边，其余的数在其右边，我们还需要把
              寻找范围缩小，下次找的时候只在数组前面left个数中找了。

               如果left的值比k小，说明上轮partition之后，前left个数找的太少了，我们需要再往数组的后面找。

              【3】这个方法是最为巧妙的，使用大根堆的方式，维护一个包含k个最小数的大根堆，让最大值在根部，之后对于新来的序列的数，就只比较跟大根堆的根部
              关系就行了，如果比根大，那就继续遍历，如果比根小就 替换到堆顶，之后再对堆进行调整。
              这样的话堆的容量就是k，而且有个优点是不需要一次性将所有数字加载到内存中，放置内存消耗过大，方法是内存占用很小的，该方法的时间复杂度计算是：
              将时间复杂度降到以k为基数，每次调整堆的时间复杂度都是O(log^k)，那么整体时间复杂度为O(klog^{k})+O((n-k)log^k) = O(nlog^k)。

'''


#######  首先是方式二.利用partation的方法    #########

#大的控制 partition的函数
def get_solution(tinput,k):  #对于序列找到前k小的数


    n=len(tinput)

    #临界条件判断
    if k<=0 and k>n:
        return list()

    start=0
    end=n-1

    mid=partition(tinput,start,end)   #找到初始的点分割情况，首次获得 mid左的都是小于的， 右边都是大于的

    #进行多次查找，如果   要找的目标k  不是现在的mid位置时
    while k-1!=mid:
        #根据现在mid的两种情况，去对应的位置再查找
        if k-1>mid:
            start=mid+1
            mid=partition(tinput,start,end)
        elif k-1<mid:
            end=mid-1
            mid=partition(tinput,start,end)

    #当我们找到合适的mid时，  说明排序也已经基本排序完整了，至少mid 也就是k  两侧已经切分好了
    res=tinput[:mid+1]
    return res

#非常典型的  partition函数部分的实现过程
def partition(tinput,low,high):
    key=tinput[low]
    while low<high:
        while low<high and tinput[high]>=key:
            high-=1

        tinput[low]=tinput[high]

        while low<high and tinput[low]<=key:
            low+=1

        tinput[high]=tinput[low]

    #因为最后一次是用low做交换，所以使用low即可
    tinput[low]=key

    return low

#######  首先是方式三.容量为k的大根堆的方式    #########
'''
   使用python内置的堆模块   但是该模块是个 最小堆的构建，  所以需要一定方法转成最大堆.
   
   我们可以借助实现了最小堆的heapq库，因为在一个数组中，每个数取反，则最大数变成了最小数，整个数字的顺序发生了变化，所以可以给数组的每个数字取反，
   然后借助最小堆，最后返回结果的时候再取反就可以了.【也就是去负数，之后比较时候再取反回来，这样没任何影响的】
   
   
   这里对heapq 的用法熟悉下：
        【1】使用heapq.heappush()函数把值加入堆中，另外一种就是使用heap.heapify(list)转换列表成为堆结构
        【2】堆创建好后，可以通过`heapq.heappop() 函数弹出堆中最小值。
'''
import heapq
def  get_big_data(alist,k):
    max_heap=[]
    length=len(alist)

    #判断边缘条件
    if not alist or k<=0 or k>length:
        return

    k=k-1
    #开始对序列的每个元素，一个个 置反后放入到  小根堆中。
    for ele in alist:
        #取反，在参与比较 。  这样反过来是对  最小堆的直接的利用
        ele=-ele
        #如果堆容量没满时，把元素ele放入到栈中
        if len(max_heap)<=k:
            heapq.heappush(max_heap,ele) #这里的max_heap就是堆的存储体
        #如果满了的话，就  替换掉最上面的一个，并将新的压进去再做调整
        else:
            heapq.heappushpop(max_heap,ele)

    #这里是很棒的 使用 map函数和lambda函数，将负数映射回去
    return map(lambda x:-x,max_heap)

L=[1,4,5,3,34,54,6]
#这里是找到最小的3个数
print(get_big_data(L,3))









