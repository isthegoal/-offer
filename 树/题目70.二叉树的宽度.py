# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：   求树的宽度
             即树的某层所含结点数目最多, 则打印出该数字


     分析：   这里的思路非常简单，就是  利用层次遍历的思想，先逐层计算每层的节点数，从中统计出最大的节点数。

'''
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    #通过  队列层次遍历的方式，获取  层次数量
    def widthofTree(self,pRoot):
        #边界条件
        if pRoot==True:
            return 0

        #创建进行层次遍历使用的队列。      这里会在nodeQue中保存所有遍历过的结点
        nodeQue=[pRoot]

        #三个符号的定义，每一层的结点数、层级等。
        levelCount={0:1}
        level=0
        maxNum=1

        while len(nodeQue):
            #首先取出上一层的  结点。     这里也算明白了，保存结点数量的另一个作用就是为了找层内的结点
            tempQue=nodeQue[:levelCount[level]]

            #层结点统计变量
            curNodeNum=0
            #对于上一层的所有结点进行  统计和压队
            while len(tempQue)>0:
                #两个pop,这里只tempQue进行pop难道不够吗？  感觉nodeQue的pop是多余的，好吧，这个是跟nodeQue[:levelCount[level]]结合的，看来必须这样干,因为这个是跟nodeQue是没有存之前之前层的
                tempQue.pop(0)
                pNode=nodeQue.pop(0)
                if pNode.left:
                    nodeQue.append(pNode.left)
                    curNodeNum+=1
                if pNode.right:
                    nodeQue.append(pNode.right)
                    curNodeNum+=1

            #把  层数量保存到字典中去
            level+=1
            if level not in levelCount.keys:
                levelCount[level]=curNodeNum

            #最大情况的更新
            if curNodeNum>maxNum:
                maxNum=curNodeNum

        return maxNum

