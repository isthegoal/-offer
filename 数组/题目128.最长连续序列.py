# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个未排序的整数数组，找出最长连续序列的长度。要求算法的时间复杂度为 O(n)。

        示例
        输入: [100, 4, 200, 1, 3, 2]
        输出: 4
        解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

      分析：


      思路：使用哈希的方式。

      首先看题目要求O（n），所以不能用一般的排序，考虑一下特殊方法比如桶排序，发现是整数数组，也不行，
      那就只能用哈希表了，建立一个哈希表，key是区间端点，val是这段区间的长度，线性扫描输入数组，
      如果当前元素已经在哈希表里，则跳过，如果不在哈希表里，就看一下它左右两侧区间的长度left， right，
      计算出它自身的区间长度length = 1 + left + right。计算完之后更新新的左右端点的长度为，
      record[num - left] = length = record[num + right], record[num]也赋值，为了占个位子。
      比如对于样例输入：[100, 4, 200, 1, 3, 2]，100进来，99和101都不在，则建立record[100] = 1 = 1 + 0 + 0
        4进来，3和5也都不在， record[4] = 1 + 0 + 0，200同理，1进来，2和0都不在，record[1] = 1 +0 + 0
        3进来，有4没5， record[3] = 1 + 1 + 0 = 1 + record[4] + record[5]

'''
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        record = dict()
        res = 0
        for num in nums:
            if num not in record:
                left = record.get(num - 1, 0)
                right = record.get(num + 1, 0)

                length = right + left + 1

                res = max(res, length)

                for i in [num - left, num, num + right]:
                    record[i] = length

        return res
