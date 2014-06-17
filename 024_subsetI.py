'''
Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''
class Solution:
	# @param S, a list of integer
	# @return a list of lists of integer
	def subsets(self, S):
		S.sort()
		l = len(S)
		max_n = 2**l
		res = []
		for i in range(0,max_n):
			currSet = []
			mylist = list(bin(i))
			mylist = mylist[2:] # remove 0b
			mylist.reverse()
			mylen = len(mylist)
			for j in range(l, mylen, -1):
				mylist.append('0')
			for j in range(0,mylen):
				if mylist[j] == "1":
					currSet.append(S[j])
			res.append(currSet)

		return res

        
S = [0,0,1,2]

a =Solution()
print (a.subsets(S))