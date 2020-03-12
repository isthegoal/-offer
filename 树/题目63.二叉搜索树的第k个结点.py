# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
     题目：给定一颗二叉搜索树，请找出其中的第k大的结点。

                例如，
                    5
                   / \
                  3  7
                 /\ /\
                2 4 6 8 中，
                按结点数值大小顺序第三个结点的值为4。

     分析：这里主要利用到二叉搜索树的性质，   当我们对二叉搜索树进行中序遍历时，得到的序列结果就是从小到大递增的。

          二叉搜索树：左子结点的值 < 根结点的值 < 右子结点的值。

     解法：对二叉排序树进行中序遍历，在中序遍历过程中 统计累加数即可，  非常的简单。

'''

#  老习惯，树结点定义
class TreeNode():

    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

    #开始简单的正式的中序遍历即可     这里pRoot是树的结点，k是表示第几个结点
class solution:
    def __init__(self):
        self.count=0
    def KntNode(self,pRoot,k):
        #临界条件
        if not pRoot:
            return None

        #先序遍历，所以需要先看左边的。          此处需要return吗，我也不太确定哎，感觉不用吧，直接中序思路即可。
        self.KntNode(pRoot.left, k)

        #这里是 进行统计，当然如果 统计到位成功了，那这就是目标结点,找到第k个直接进行返回即可
        self.count+=1
        if self.count==k:
            return pRoot

        #先序的后部分，  我们再看下右边的
        self.KntNode(pRoot.right, k)
