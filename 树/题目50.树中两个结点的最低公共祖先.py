'''
     ��Ŀ�� ����ͨ������������������͹�������

     ������ �м���˼·�ɣ�����Ҫ˼���������ȣ���ȻҪ���������ˣ�����������Ҫ�ķ����ǣ�
           [1].�ȱ������ ������㵽���ڵ��·����Ȼ���·���������ҳ���� һ��������㡣
'''

class Solution(object):
    def __init__(self,root,node1,node2):
        self.root=root
        self.node1=node1
        self.node2=node2

    # ��ȡ ·����  root�����Ķ��ˣ�  node�ǵ�ǰ���к����Ľ��   ʹ��ret�����ռ���·��
    def get_path(root,node,ret):
        if not node or not node:
            return False

        #�ȽϺ��ĵ� �������ߵ�·�����б���
        ret.append(root)

        #�ж�   �Ƿ񵽴� �Ӹ�������Ŀ����
        if root==node:
            return True

        #�ݹ������ ������ ���� ����
        left=Solution.get_path(root.left,node,ret)
        right=Solution.get_path(root.right,node,ret)
        if left or right:
            return True

        #�ϲ��裬�� ���һ��������һЩ���ڵĽ����жϺ��  ret�洢������pop
        ret.pop()

    def get_last_common_node(self):
        #�ֱ��ȡ  ����Ŀ����� ����·��
        route1=[]
        route2=[]

        #����·���ռ���ɡ�
        ret1=Solution.get_path(self.root,self.node1,route1)
        ret2 = Solution.get_path(self.root, self.node2, route2)

        #���ղغõ�·�������зֱ�ıȽϡ�������бȽ�ʱ����
        ret=None
        if ret1 and ret2:
            #��������  ·�����ϵıȽ�   ��Ϊ  ����С����ƫ�����ֵģ�����ֻ��Ҫ��ǰ����ȥ��������
            length=len(route1) if len(route1)<len(route2) else len(route2)



            #  ������·�ɣ��ҵ���·���ģ� ��ǰ��������ͳ�ƾ����ˡ�  ��ͬ�ľ��ǹ���·��.....
            index=0
            while index<length:
                if route1[index]==route2[index]:
                    ret=route1[index]
                index+=1
            return ret

