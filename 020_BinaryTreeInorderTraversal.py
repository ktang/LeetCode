# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def inorderTraversal(self, root):
		p = root
		S= []
		l = []
		if p == None:
			return l
		
		while (p != None or len(S) != 0):
			if p!=None:
			#	l.append(p.val)
				S.append(p)
				p = p.left
				
			else:
				p = S.pop()
				l.append(p.val)
				p = p.right
		return l
		
	def inorderTraversal2(self, root):
		if root == None:
			return []
		return self.inorderTraversal2(root.left) +  [root.val] +self.inorderTraversal2(root.right)
'''
class Solution:
	# @param root, a tree node
	# @return a list of integers
	def inorderTraversal2(self, root):
		if root == None:
			return []
		return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
'''        
a =Solution()
tree = TreeNode("A")
tree.right = TreeNode("C")
tree.left = TreeNode("B")
tree.left.left=TreeNode("D")

tree.left.right = TreeNode("E")
tree.left.right.left = TreeNode("F")
tree.left.right.left.right = TreeNode("V")
tree.left.right.left.left = TreeNode("W")
print a.inorderTraversal(tree)

print a.inorderTraversal2(tree)
