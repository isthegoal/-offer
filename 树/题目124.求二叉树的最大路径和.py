# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个非空二叉树，返回其最大路径和。
            本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

            例输入: [1,2,3]
               1
              / \
             2   3
            输出: 6

            例输入: [-10,9,20,null,null,15,7]
            	 -10
                 / \
               9    20
              /  \
             15   7
            输出: 42


      分析：



      思路：

         对于任意一个节点, 如果最大和路径包含该节点, 那么只可能是两种情况:
        （1）其左右子树中所构成的和路径值较大的那个（如果左子树或右子树构成的最大路径和为负数，则置为零，
        表示最大路径不经过这个子树）加上该节点的值后向父节点回溯构成最大路径，也可能没有左右子树，只有该节点的值往前回溯。
        （2）左右子树都在最大路径中, 加上该节点的值构成了最终的最大路径。即，该节点是最大路径的根节点。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):    # 定义一个result属性
        self.result = float("-inf")
    def maxPathSum(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.getMax(root)
        return self.result
    def getMax(self,root):  # 定义一个辅助函数
        if root == None:  # 如果当前节点为空就表示包含当前节点的最大路径为0
            return 0
        # 递归的计算当前节点的左子树和右子树能提供的最大路径和，如果为负，就置为零（和0比较）
        left = max(0,self.getMax(root.left))
        right = max(0,self.getMax(root.right))
        # 每计算一次左右子树的最大值，就更新当前的result
        self.result = max(self.result,left + right + root.val)
        # 往父节点回溯的话，最大路径就不能同时包含左右两个子树，
        # 因此需要用左右子树较大的那个子树加上当前节点的值进行回溯
        return max(left,right) + root.val
        #（递归函数，返回的是回溯需要的式子，而不是返回最终结果（比如这里的 return result））
