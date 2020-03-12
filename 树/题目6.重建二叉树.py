# coding: utf-8

'''
     就是一般的   数据结构的问题，利用 前序遍历结果  和  中序遍历结果来确定一棵树

     思路：前序的第一个元素是根结点的值，在中序中找到该值，中序中该值的左边的元素是根结点的左子树，右边是右子树，然后递归的处理左边和右边

     根本思想还是 利用树的性质做  递归，很简单的递归【不断延伸完成树的构建】
'''
class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def construct_tree(preorder=None,inorder=None):

    # 首先是递归截止条件
    if not preorder or not inorder:
        return None


    #根据  先序遍历的位置找到 根节点。
    index=inorder.index(preorder[0])
    left=inorder[0:index]
    right=inorder[index+1:]

    #创建节点树   (不断嵌入搭建好整个树，注意  一个树下前序和中序的长度肯定是一致的)
    root=TreeNode(preorder[0])
    root.left=construct_tree(preorder[1:1+len(left)],left)
    root.right=construct_tree(preorder[-len(right)],right)
    return root
