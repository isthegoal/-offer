'''
     题目： 求普通二叉树中两个结点的最低公共祖先

     分析： 有几种思路吧，不过要思考公共祖先，当然要遍历祖先了，所以这里主要的方法是：
           [1].先遍历求出 两个结点到根节点的路径，然后从路径集合中找出最后 一个公共结点。
'''

class Solution(object):
    def __init__(self,root,node1,node2):
        self.root=root
        self.node1=node1
        self.node2=node2

    # 获取 路径，  root是树的顶端，  node是当前进行衡量的结点   使用ret保存收集的路径
    def get_path(root,node,ret):
        if not node or not node:
            return False

        #比较核心的 ，对行走的路径进行保存
        ret.append(root)

        #判断   是否到达 从根到达了目标结点
        if root==node:
            return True

        #递归的往左 和往右 进行 查找
        left=Solution.get_path(root.left,node,ret)
        right=Solution.get_path(root.right,node,ret)
        if left or right:
            return True

        #老步骤，在 最后一步，对于一些现在的进行判断后的  ret存储器进行pop
        ret.pop()

    def get_last_common_node(self):
        #分别获取  两个目标结点的 祖先路径
        route1=[]
        route2=[]

        #进行路径收集完成。
        ret1=Solution.get_path(self.root,self.node1,route1)
        ret2 = Solution.get_path(self.root, self.node2, route2)

        #对收藏好的路径，进行分别的比较【这里进行比较时，】
        ret=None
        if ret1 and ret2:
            #进行两个  路径集合的比较   因为  索引小的是偏根部分的，所以只需要从前往后去索引即可
            length=len(route1) if len(route1)<len(route2) else len(route2)



            #  基本套路吧，找到下路径的， 从前往后索引统计就行了。  相同的就是公共路径.....
            index=0
            while index<length:
                if route1[index]==route2[index]:
                    ret=route1[index]
                index+=1
            return ret

