'''
Merge Two Sorted Lists Total Accepted: 11114 Total Submissions: 34658
Merge two sorted linked lists and return it as a new list. The new 
list should be made by splicing together the nodes of the first two lists.

#1
class Solution:
# @param two ListNodes
# @return a ListNode
 def mergeTwoLists(self, l1, l2):
  if l1 == None:
   return l2
  if l2 == None:
   return l1

  l1_p = l1
  if l2.val < l1.val:
   tmp = l2
   l2  = l1
   l1  = tmp
   l1_p = l1

  while l2 != None:
   if l1_p != None and l1_p.val < l2.val:
    if l1_p.next != None and l1_p.val >= l2.val:
     tmp = l2
     l2=l2.next
     tmp.next = l1_p.next
     l1_p.next = tmp
     l1_p = l1_p.next
    elif l1_p.next != None and l1_p.val < l2.val:
     assert False
   if l1_p.next ==None:
    l1_p.next = l2
    return l1
  return l1
#################
#Runtime Error Message:	Line 32: AssertionError
#Last executed input:	{5}, {1,2,4}



#2
201 / 208 test cases passed.
Status: Wrong Answer
Submitted: 0 minutes ago
Input:	{2}, {1}
Output:	{1}
Expected:	{1,2}

class Solution:
# @param two ListNodes
# @return a ListNode
	def mergeTwoLists(self, l1, l2):
		if l1 == None:
			return l2
		if l2 == None:
			return l1
		l1_p = l1
		if l2.val < l1.val:
			tmp = l2
			l2  = l1
			l1  = tmp
			l1_p = l1

		while l2 != None:
			if l1_p != None and l1_p.val <= l2.val:
				if l1_p.next != None and l1_p.next.val > l2.val:
					tmp = l2
					l2=l2.next
					tmp.next = l1_p.next
					l1_p.next = tmp
					l1_p = l1_p.next
					if l2 == None:
						break
				else: 
					l1_p = l1_p.next
			if l1_p == None:
  				break
			if l1_p.next == None:
				l1_p.next = l2
				return l1
		return l1
'''

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def print_list(l):
	while l != None:
		print l.val
		l=l.next

class Solution:
# @param two ListNodes
# @return a ListNode
	def mergeTwoLists(self, l1, l2):
		if l1 == None:
			return l2
		if l2 == None:
			return l1
		l1_p = l1
		if l2.val < l1.val:
			tmp = l2
			l2  = l1
			l1  = tmp
			l1_p = l1

		while l2 != None:
			if l1_p != None and l1_p.val <= l2.val:
				if l1_p.next != None and l1_p.next.val > l2.val:
					tmp = l2
					l2=l2.next
					tmp.next = l1_p.next
					l1_p.next = tmp
					l1_p = l1_p.next
					if l2 == None:
						break
				elif l1_p.next!=None: 
					l1_p = l1_p.next
			if l1_p == None:
  				break
			if l1_p.next == None:
				l1_p.next = l2
				return l1
		return l1

'''					
#{5}, {1,2,4}
#l1 = ListNode(5)
#l2 = ListNode(1)
#l2.next = ListNode(2)
#l2.next.next = ListNode(4)	
'''
'''
#{-10,-10,-9,-4,1,6,6}, {-7}	
l1 = ListNode(-10)
l1.next = ListNode(-10)
l1.next.next = ListNode(-9)
l1.next.next.next = ListNode(-4)
l1.next.next.next.next = ListNode(1)
l1.next.next.next.next.next = ListNode(6)
l1.next.next.next.next.next.next = ListNode(6)

l2 = ListNode(-7)
'''

'''
#{-10,-9,-6,-4,1,9,9}, {-5,-3,0,7,8,8}
l1 = ListNode(-10)
l1.next = ListNode(-9)
l1.next.next = ListNode(-6)
l1.next.next.next = ListNode(-4)
l1.next.next.next.next = ListNode(1)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(-5)
l2.next = ListNode(-3)
l2.next.next = ListNode(0)
l2.next.next.next = ListNode(7)
l2.next.next.next.next = ListNode(8)
l2.next.next.next.next.next = ListNode(8)
'''

l1 = ListNode(2)
l2 = ListNode(1)

print "l1"
print_list(l1)
print "l2"
print_list(l2)
a =Solution()

print " "
print "res"
print ""

h= a.mergeTwoLists(l1, l2)
print_list(h)