'''
Roman to Integer Total Accepted: 6638 Total Submissions: 20514
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution:
	# @return an integer
	def romanToInt(self, s):
		dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "0":0}
		x = s + "0"
		num = 0
		
		a = list(x)
		for i in range(0,len(a)):
			digit = a[i]
			if digit != "0":
				next_digit = a[i+1]
				this_num = dict[digit]
				next_num = dict[next_digit]
				if this_num < next_num:
					num -= this_num
				else: num+=this_num
				
		return num
		

a =Solution()
print a.romanToInt("IV")

print a.romanToInt("MMXIV")