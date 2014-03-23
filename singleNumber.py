'''Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

#Status: Time Limit Exceeded
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        tmp = {}
        for i in A:
            if i in tmp.keys():
            	del tmp[i]
            else:
            	tmp[i] = 1
        return tmp.keys()[0]
'''
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        single_num = 0
        for i in A:
            single_num = single_num ^ i
        return single_num

a = Solution()
print a.singleNumber([1,3, 1])