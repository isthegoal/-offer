# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，
           第三行按照从左到右的顺序打印，其他行以此类推。


     分析：首先这很明显的是一种层次遍历，为了实现层次遍历，我们使用栈的方式。

     可以使用两个栈，对两个栈的利用方式是：
        （1）如果当前打印的是奇数层时，则先保存左子树结点再保存右子树结点到第一个栈。【因为是之字形，之后栈弹出后就可以从右到左】
        （2）如果当前打印的是偶数层的话，则先保存右子树结点再保存左子树结点到第二个栈

    注意这里有两个栈，而且必须得用两个栈，因为 栈中会有层的残余。

'''
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class solution:
    def Print(self,pRoot):

        #用来保存打印结果的  数组。
        resultArrary=[]
        if not pRoot:
            return resultArrary

        curLayerNodes=[pRoot]
        isEvenLayer=True

        #如果栈不为空，就需要一直往下打印
        while curLayerNodes:

            #这里   使用两个栈进行保存，   记住这两个栈有很大的区别，一个是先存储的栈curLayerNodes，  另一个是后续的使用存储nextLayerNodes。
            #此外这里 curLayerValues是用于存储 该层可以打印的值，
            #核心就是四个东西吧    curLayerNodes：当前层的结点    nextLayerNodes：下一层结点  isEvenLayer：是奇数还是偶数层   curLayerValues：当前层用于打印的信息
            curLayerValues=[]
            nextLayerNodes=[]
            isEvenLayer=not isEvenLayer

            #这就是  第一个栈的作用了，就是对于   第一个栈中的所有元素   进行一个个的放到第二个栈中，同时实现遍历和 遍历结果往栈放置的效果。
            for node in curLayerNodes:
                curLayerValues.append(node.val)
                #对下层的孩子保存，这里是使用相同的保存方式，而在后面打印时，设置和前序、后序两种性质，实现的效果是一样的。
                if node.left:
                    nextLayerNodes.append(node.left)
                if node.right:
                    nextLayerNodes.append(node.right)

            curLayerNodes=nextLayerNodes

            #这里是核心的 控制需要 打印信息的存储。   这里如果是奇数层就正着用，如果是偶数层就反正用。   这样的方式来控制信息的存储。
            resultArrary.append(curLayerValues[::-1]) if isEvenLayer else resultArrary.append(curLayerValues)

        #当 要打印的收集结束后，  直接把结果进行返回即可。
        return resultArrary


