# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精
'''
     题目：统计一个数字在排序数组中出现的次数。

     分析：首先这里从题意上 就能发现一些特别的性质可以利用。   1.有序、2.数组、3次数统计

          所以可以得知对于每个数其重复的数肯定是在一起的，因此不需要逐个遍历，只需要按照这个性质尽心查找就行了。需要查找到两个位置点：
           【1】对于目标数字所处的一个索引位，其前面的索引位数字都是  小于该数的
           【2】对于目标数字所处的一个索引位，其后面的索引位数字都是  大于该数的

    所以这里就明显牵扯到查找问题了，在查找方法中，最典型的方式就是  折半查找，我们使用那一思路吧，用两次折半来获取索引位
'''
#该函数   是主要的获取  上面说的位置点，并计算出位置索引差
def main(nums,k):
    first=get_first_k(nums,k)
    last=get_last_k(nums,k)

    #在获取索引位后，对差值进行计算
    if first<0 and last<0:
        return 0
    if first<0 or last<0: #容易忽略的一点，有一个为负值，emm...
        return 1

def get_first_k(nums,k):
    #使用折半查找   找到第一索引位
    left,right=0,len(nums)-1
    while left<right:
        mid=(left+right)/2
        #该往右查找的情况
        if nums[mid]<k:
            #此时如果发现  再往后以为就是我们需要的数时，这个位置就是我们需要的
            if mid+1<len(nums) and nums[mid+1]==k:
                return mid+1
            #正常往右走
            left=mid+1
        #第二种情况，需要看之前的是否是这个数即可
        elif nums[mid]==k:
            #这里可以考虑下只有单位数的情况
            if mid-1<0 or (mid-1>=0 and nums[mid-1]<k):
                return mid
            right=mid-1

        #第三种情况   就是nums>k的情况，那么肯定直接需要往左走即可
        else:
            right=mid-1

    #最后找不到时候
    return -1

def get_last_k(nums,k):   #好吧，该出就照着之前的略微修改吧
    #使用折半查找   找到第一索引位
    left,right=0,len(nums)-1
    while left<right:
        mid=(left+right)/2
        if nums[mid]<k:
            left = mid + 1

        elif nums[mid]==k:
            if mid+1==len(nums) or (mid+1<len(nums) and nums[mid+1]>k):
                return mid
            left=mid+1
        else:
            if mid-1>=0 and nums[mid-1]==k:
                return mid
            #正常往左走
            right=mid-1

    #最后找不到时候
    return -1
