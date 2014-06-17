# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def postorderTraversal(self, root):
		p = root
		S= []
		S2 = []
		l = []
		if p == None:
			return l
		#dir = ""
		while (p != None or len(S) != 0):
			if p!=None:
			#	l.append(p.val)
				S.append(p)
				p = p.left
				dir = "l"
			else:
				p = S.pop()
				#l.append(p.val)
			#	if ( p.right == None):
			#		l.append(p.val)
			#	else:
			#	if len(S2) != 0 and dir == "r":
			#		l.append(S2.pop().val)
				S2.append(p)
				p = p.right
				if p == None:
					while len(S2) != 0:
						l.append(S2.pop().val)
				#dir = "r"
		while len(S2) != 0:
			l.append(S2.pop().val)
		return l
		
	def inorderTraversal2(self, root):
		if root == None:
			return []
		return self.inorderTraversal2(root.left) +self.inorderTraversal2(root.right) +  [root.val] 
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
print a.postorderTraversal(tree)

print a.inorderTraversal2(tree)

tree2 = TreeNode("A")
tree2.right = TreeNode("C")
tree2.left = TreeNode("B")
tree2.left.left=TreeNode("D")
tree2.left.right = TreeNode("E")
print a.postorderTraversal(tree2)
print a.inorderTraversal2(tree2)
