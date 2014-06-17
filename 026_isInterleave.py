'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

class Solution:
	# @return a boolean
	def isInterleave(self, s1, s2, s3):
		l1 = len(s1)
		l2 = len(s2)
		l3 = len(s3)
		if l1+l2!=l3:
			return False

		a1= list(s1)
		a2= list(s2)
		a3= list(s3)

		a3.reverse()
		curr = ""
		while a3 != []:
			curr += a3.pop()
			currl = len(curr)
			c1 = "".join(a1[0:currl])
			c2 = "".join(a2[0:currl])

			print c1
			print c2
			print curr

			if c1 == c2:
				if curr != c1:
					return False
			elif curr == c1:
				a1 = a1[currl:]
				curr=""
			elif curr == c2:
				a2 = a2[currl:]
				curr=""
			else:
				return False
		return True

Input:	"aa", "ab", "aaba"
Output:	false
Expected:	true

Submission Result: Time Limit Exceeded

Last executed input:	"bacbacbabacbab", "bbbcaacaacba", "bbabcbbacacabcbacbaaaabbac"

"bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
#4m36.022s
l1 = len(s1)
		l2 = len(s2)
		l3 = len(s3)
		if l1+l2!=l3:
			return False

		if l1==0:
			return s2==s3
		elif l2 == 0:
			return s1==s3
		else:
			if s1[0] != s3[0] and s2[0] != s3[0]:
				return False
			if s1[-1] != s3[-1] and s2[-1] != s3[-1]:
				return False
			if s1[0] != s3[0]:
				return self.isInterleave(s1, s2[1:], s3[1:])
			elif s2[0] != s3[0]:
				return self.isInterleave(s1[1:], s2, s3[1:])
			else:
				return self.isInterleave(s1, s2[1:], s3[1:]) or self.isInterleave(s1[1:], s2, s3[1:])

Stack<Object> stack;
stack.push(first_object);
while( !stack.isEmpty() ) {
   // Do something
   my_object = stack.pop();

  // Push other objects on the stack.

}
class Solution:
	# @return a boolean
	def isInterleave(self, s1, s2, s3):
		myStack = []
		myStack.append((s1, s2, s3))
		myRes = False
		while myStack!=[]:
			mys1, mys2, mys3 = myStack.pop()
			l1 = len(mys1)
			l2 = len(mys2)
			l3 = len(mys3)
			#if l1+l2!=l3:
				#return False

			if l1==0:
				if mys2==mys3:
					myRes = True
			elif l2 == 0:
				if mys1==mys3:
					myRes = True
			else:
				
				# if mys1[0] != mys3[0] and mys2[0] != mys3[0]:
				# 	return False
				# if mys1[-1] != mys3[-1] and mys2[-1] != mys3[-1]:
				# 	return False
				# if mys1[0] != mys3[0]:
				# 	myStack.append((mys1, mys2[1:], mys3[1:]))
				# elif mys2[0] != mys3[0]:
				# 	myStack.append((mys1[1:], mys2, mys3[1:]))
				# else:
				
				myStack.append((mys1, mys2[1:], mys3[1:]))
				myStack.append((mys1[1:], mys2, mys3[1:]))
			
		return myRes

DP problem:
f[i][j] represents the T/F value for the first i-th and j-th of str1 and
str2

f[i][j] = (str1[i] == str3[i+j] and f[i-1][j] == T ) or
		  (str2[j] == str3[i+j] and f[i][j-1] ==T)


'''
class Solution:
	# @return a boolean
	def isInterleave(self, s1, s2, s3):
		def ini_2d_list(f,l1,l2):
			for i in range(l1 + 1 ):
				tmp = []
				for j in range(l2 + 1):
					tmp.append(None)
				f.append(tmp)

		l1 = len(s1)
		l2 = len(s2)
		l3 = len(s3)
		if l1+l2!=l3:
			return False
		f=[]
		ini_2d_list(f,l1,l2);
		f[0][0]=True
		for i in range(1,l1 + 1):
			f[i][0] = s1[i-1] == s3[i-1]
		for j in range(1, l2 + 1):
			f[0][j] = s2[j-1] == s3[j-1]

		for i in range(1, l1+1):
			for j in range(1, l2+1):
				f[i][j] = (s1[i-1] == s3[i+j-1] and f[i-1][j] == True ) or (s2[j-1] == s3[i+j-1] and f[i][j-1] ==True)

		return f[l1][l2]

		
		#if l1+l2!=l3:
		#	return False
		# if l1==0:
		# 	return s2==s3
		# if l2==0:
		# 	return s1==s3

a =Solution()

print a.isInterleave("a", "", "c")
print a.isInterleave("a", "b", "a")
print a.isInterleave("aacaac", "aacaaeaac", "aacaaeaaeaacaac")#F
print a.isInterleave("aa", "b", "abba")

'''
s1="aa"
s2="ab"
s3="aaba"
print a.isInterleave(s1, s2, s3)# T


l1= "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
l2= "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
l3= "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"

#False
print a.isInterleave(l1, l2, l3) #F

print a.isInterleave("bacbacbabacbab", "bbbcaacaacba", "bbabcbbacacabcbacbaaaabbac")

print a.isInterleave("aa", "bb", "abba")
print a.isInterleave("aa", "bb", "abab")
print a.isInterleave("aa", "bb", "bbaa")


s1 = "aaaabcc"
s2 = "dbbca"
s3 = "aaaadbbcbcac"
#print s1
#print s2
#print s3
print a.isInterleave(s1, s2, s3)

s3 = "aadbbbaccc"
#print s1
#print s2
#print s3
print a.isInterleave(s1, s2, s3)
'''