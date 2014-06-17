'''
Longest Common Prefix Total Accepted: 10995 Total Submissions: 40635 My Submissions
Write a function to find the longest common prefix string amongst an array of strings.
'''

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
    	def all_have(i,prefix,strs):
    		for s in strs:
    			if (s[0:i]!=prefix):
    				return False
    		return True

        if len(strs) == 0:
        	return "" # change from None to ""
        
        min_n = len(strs[0])
        min_str = strs[0]
        for s in strs:
        	l = len(s)
        	if l < min_n:
        		min_n = l
        		min_str = s

        for i in range(min_n,0,-1):
        	prefix = min_str[0:i]
        	if all_have(i,prefix,strs):
        		return prefix

        return "" # change from None to ""



s = ['cabc','abi','ab']

a =Solution()
print a.longestCommonPrefix(s)