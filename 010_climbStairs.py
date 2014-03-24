'''
Climbing Stairs Total Accepted: 10248 Total Submissions: 31480
Total Accepted: 10249 Total Submissions: 31481

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
    	if n == 0:
    		return 1
    	if n == 1:
    		return 1
    	last2 = 1
    	last1 = 1
    	num = 0
    	for i in range(1,n):
    		num = last1 + last2
    		last2 = last1
    		last1 = num
    	return num
    	

a =Solution()
print a.climbStairs(0)
print a.climbStairs(1)
print a.climbStairs(2)
print a.climbStairs(3)
print a.climbStairs(4)
print a.climbStairs(5)