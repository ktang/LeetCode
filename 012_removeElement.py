'''
Remove Element Total Accepted: 10732 Total Submissions: 33297
Total Accepted: 10732 Total Submissions: 33300
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

#1 Wrong Answer
Input:	[4,5], 4
Output:	[4]
Expected:	[5]
 def removeElement(self, A, elem):
        l = []
        for i in A:
            if (i == elem):
                continue
            else:
                l.append(i)
        A = l
        return len(A)
        
        
#2
Runtime Error Message:	Line 26: TypeError: range() integer end argument expected, got list.
Last executed input:	[], 0
 def removeElement(self, A, elem):
        l = []
        for i in A:
            if (i == elem):
                continue
            else:
                l.append(i)
        
        return l
        
        
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        l = []
        for i in A:
            if (i == elem):
                continue
            else:
                l.append(i)
        A = l
        return len(A)

a =Solution()
print a.()        
'''
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        l = []
        for i in A:
            if (i == elem):
                continue
            else:
                l.append(i)
        return len(l)
        