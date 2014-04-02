# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def preorderTraversal(self, root):
		p = root
		S= []
		l = []
		if p == None:
			return l
		
		while (p != None or len(S) != 0):
			if p!=None:
				l.append(p.val)
				S.append(p)
				p = p.left
				
			else:
				p = S.pop()
				p = p.right
		return l
'''
class Solution:
	# @param root, a tree node
	# @return a list of integers
	def preorderTraversal(self, root):
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
print a.preorderTraversal(tree)

print a.KaipreorderTraversal(tree)
