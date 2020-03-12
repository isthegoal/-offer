# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
     题目：   判断给定的整数数组是不是二叉搜索树的后序遍历序列，  同时设定了整数数组中不包含重复值

     分析：   这道题直观上进行观察，  可以发现两个重要的点：  二叉搜索树、  后续遍历序列。
              可以使用两者的性质来对序列进行验证。

              具体实现上，还是使用递归的方法，主要从两个点上进行突破：
                  【1】后续遍历的最后一个值是根结点
                  【2】比根结点小的值都是  左子树的值，  剩下的都应该是右子树的值。
              所以可以依据以上两点，不断进行递归方式的检验即可
     思路：    思路就是   两大部分把，分别是   当前后序情况的验证   和   进行分离下来每一部分 满足后续遍历的特点。

'''
def is_post_order(order):
    length=len(order)

    #如果 当前 位置子问题的 序列 是大于0的
    if length:
        #  接下来分为三步，首先看最后一个值，  最后一个值可以做一种分离， 其左边子树都小于该值， 右边子树都大于该值
        # 第一步
        root=order[-1]

        #第二步，左边子树都小于该值的验证
        left=0
        while order[left]<root:
            left+=1

        #第三步，从该left开始后的 每个值，都应该是 大于root值的，核心的 验证思想
        right=left
        while right<length-1:
            if order[right]<root:
                return False
            right+=1

        #  接下来是第二部分，在大的部分满足后，看每个小的每个部分是否同样满足，这是最能直观体现递归作用的地方
        left_ret=True if left==0 else is_post_order(order[:left])  #以这里的left为新的  终点去看
        right_ret=True if left==right else is_post_order(order[left:right])

        #对于左右两个细节部分，需要同时满足性质才可以
        return left_ret and right_ret
    return False
