# coding: utf-8


'''
     题目：  把递增数组的前面部分数字移到队尾，求数组中的最小值，例如[3,4,5,6,1,2]      【意思是 对于有这种特性的数组，找到最小值,但是我感觉直接min不就行了】

     方案：  使用二分查找，  核心是找到那个左侧 大于右侧的点。
              先确定中间值，如果左侧  < 中间值，  说明在  （中间值，右侧）之间
                           如果右侧  > 中间值    说明在  （左侧，中间值）之间

'''
def find_min(arr):
    if not arr:
        return False

    length=len(arr)
    left,right=0,length-1

    while arr[left]>=arr[right]: #必须满足这一性质，才在这之间
        # 二分查找的截止条件。
        if right-left==1:
            return arr[right]

        mid=(right+left)/2
        if arr[left]<mid:
            left=mid
        elif arr[right]>mid:
            right=mid
    return arr[right]
