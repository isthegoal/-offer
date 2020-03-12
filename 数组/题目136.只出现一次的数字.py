# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

      示例 1:
        输入: [2,2,1]
        输出: 1

      分析：


      思路： 这个是非常经典也是  非常常见，但是 不怎么会被考到的题目。  直接根据二进制的异或思路解决即可。

      异或性质为：A^B^B = A

'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res
