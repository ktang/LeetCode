'''
Single Number II Total Accepted: 10950 Total Submissions: 34053
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

'''
http://www.quora.com/Algorithms/Given-an-integer-array-such-that-every-element-occurs-3-times-except-one-element-which-occurs-only-once-how-do-I-find-that-single-element-in-O-1-space-and-O-n-time-complexity/answer/Anders-Kaseorg/comment/2686804
http://www.geeksforgeeks.org/find-the-element-that-appears-once/
Run a loop for all elements in array. At the end of every iteration, maintain following two values.
ones: The bits that have appeared 1st time or 4th time or 7th time .. etc.
twos: The bits that have appeared 2nd time or 5th time or 8th time .. etc.
Finally, we return the value of ‘ones’
How to maintain the values of ‘ones’ and ‘twos’?
‘ones’ and ‘twos’ are initialized as 0. For every new element in array, find out the common set bits in the new element and previous 
value of ‘ones’. These common set bits are actually the bits that should be added to ‘twos’. So do bitwise OR of the common set bits with 
‘twos’. ‘twos’ also gets some extra bits that appear third time. These extra bits are removed later.
Update ‘ones’ by doing XOR of new element with previous value of ‘ones’. There may be some bits which appear 3rd time. These extra bits
 are also removed later.

Both ‘ones’ and ‘twos’ contain those extra bits which appear 3rd time. Remove these extra bits by finding out common set bits in ‘ones’ and ‘twos’.
'''
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        single_num = 0
        for i in A:
            single_num = single_num | i
        return single_num

a =Solution()
print a.singleNumber([1,2,1,3,1,2,2,7,7,7])