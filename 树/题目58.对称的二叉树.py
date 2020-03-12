# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：实现一个函数，用来判断一颗二叉树是不是对称的。
          注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

     分析： 这里的基本思想还是使用遍历的方法，通过设定两种遍历进行比较。
     这里引入一种新的遍历方式叫做 对称遍历： 其基本思路是会在前序遍历的基础上， 先遍历右子节点再遍历左子节点。

     这样我们只需要比较先序遍历和 对称遍历即可。具体的例子可以参考 https://cuijiahua.com/blog/2018/01/basis_58.html

     这里有个问题是需要应对部分为空的情况，这样的情况中，是无法通过遍历比较察觉出来的，所以需要把为Null的情况也考虑在内。对叶子结点，
     对其左右为null的树取值也做保留。


     此外在具体实现遍历时，还分递归方法和非递归方法。

'''

#首先定义下 树结构
class Treenode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
# 定义进行对称遍历 判别的核心类
class Solution:
    #主要的  调用启动函数
    def isSymmetrical(self,pRoot):
        if not pRoot:
            return True
        return self.recursiveTree(pRoot.left,pRoot.right)

    #对先序遍历和 对称遍历进行 判别 比较 相同的函数。   但是这个方式还是挺牛逼的，需要参考下
    #这里分离的左和右  是因为我们是考虑对称，最左和最右应该是对称的，此外我们也需要如果是Null的,应该左右对称着Null
    def recursiveTree(self,left,right):
        #这里是对null空的情况的考虑，如果出现空，也需要左右对称的null
        if not left and not right:
            return True
        if not left or not right:
            return False

        #针对于 非空  且值对称相同的情况，我们继续往下看， 需要往左和  往右 绝对得对称。
        if left.val==right.val:
            return self.recursiveTree(left.left,right.right) and self.recursiveTree(left.right,right.left)

        return False

if __name__=='__main__':

    #创建结点。
    A1=Treenode(1)
    A2=Treenode(2)
    A3=Treenode(3)
    A4=Treenode(4)
    A5=Treenode(5)

    #构建树结点联系。
    A1.left=A2
    A1.right=A3
    A2.left=A4
    A2.right=A5

    #最后的决策判断即可
    solution=Solution()
    ans=solution.isSymmetrical(A1)
    print(ans)