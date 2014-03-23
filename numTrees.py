'''
Unique Binary Search Trees
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   
#1 Wrong Answer
Input:	4
Output:	12
Expected:	14

class Solution:
    # @return an integer
    def numTrees(self, n):
    	if n == 0:
    		return 0
    	if n == 1:
    		return 1
    	if n == 2:
    		return 2
    	num_tree = [0, 1]
    	for i in range(2, n + 1):
    		num_tree.append( num_tree[i-2] + 2 * num_tree[i-1])
    	return num_tree[n]
   
'''
'''
Catalan number
prod ((n+k)/k) k =2..n

T(n+1) = (4n + 2)/ (n+2) * T(n)

'''
class Solution:
    # @return an integer
    def numTrees(self, n):
    	if n == 0:
    		return 1
    	last_num = 1
    	num = 1
    	for i in range(0, n):
    		num = last_num * (4 * i + 2) / (i + 2) 
    		last_num = num
    	return num

a =Solution()
print a.numTrees(0)
print a.numTrees(1)
print a.numTrees(2)
print a.numTrees(3)
print a.numTrees(4)
print a.numTrees(5)
print a.numTrees(6)
print a.numTrees(7)
print a.numTrees(8)
print a.numTrees(9)