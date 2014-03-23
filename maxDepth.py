'''
Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#1 Line 12: NameError: global name 'isLeaf' is not defined
class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
    	if isLeaf(root):
    		return 1
    	else:
    		right_dep, left_dep = 0
    		if(root.right != None):
    			rigth_dep = maxDepth(root.right)
    		if(root.left != None):
    			left_dep = maxDepth(root.left)
    		return max(rigth_dep, rigth_dep) + 1
    	
#2 Line 15: AttributeError: 'NoneType' object has no attribute 'left'
class Solution:
    # @param root, a tree node
    # @return an integer
    
    
    def maxDepth(self, root):
    	def isLeaf(root):
    		if(root.left == None and root.right == None):
    			return True
    		return False
    	
    	def max(A,B):
    		if(A>=B):
    			return A
    		else:
    			return B
    
    	if isLeaf(root):
    		return 1
    	else:
    		right_dep, left_dep = 0, 0
    		if(root.right != None):
    			right_dep = self.maxDepth(root.right)
    		if(root.left != None):
    			left_dep = self.maxDepth(root.left)
    		return max(right_dep, left_dep) + 1
'''

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    
    
    def maxDepth(self, root):
    	def isLeaf(root):
    		if(root.left == None and root.right == None):
    			return True
    		return False
    	
    	def max(A,B):
    		if(A>=B):
    			return A
    		else:
    			return B
		
		if root == None:
			return 0    
    
    	if isLeaf(root):
    		return 1
    	else:
    		right_dep, left_dep = 0, 0
    		if(root.right != None):
    			right_dep = self.maxDepth(root.right)
    		if(root.left != None):
    			left_dep = self.maxDepth(root.left)
    		return max(right_dep, left_dep) + 1
    	
root = TreeNode(1)

left = TreeNode(2)
root.left = left

a =Solution()

print a.maxDepth(root)