'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''

'''
Time Limit Exceeded
class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
    	visitedNodes = []
    	
    	if head == None:
    		return False    	
    	if head.next == None:
    		return False
    	
    	while head != None and head.next != None:
    		if head.next in visitedNodes:
    			return True	
    		if head != None:
	    		visitedNodes.append(head)
    		else:
    			return False
    		head = head.next	
    		
    	return False
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
    '''
    two points, one move one step and second moves
    two steps, if there is a circle, P2 can reach
    P1.
    '''   	
    	
    	if head == None:
    		return False
    	
    	if head.next == head:
    		return True
    	
    	if head.next == None:
    		return False
    	
    	if head.next.next == None:
    		return False
    		
    	P1 = head.next
    	P2 = head.next.next
    	
    	while P2 != None and P2.next != None:
    		if(P1 == P2 and P1 != None):
    			return True
    		P1 = P1.next
    		P2 = P2.next.next
    	
    	return False
    	

a =Solution()
print a.()