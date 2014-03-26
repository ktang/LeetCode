'''
Integer to Roman Total Accepted: 6260 Total Submissions: 19425
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''


class Solution:
	# @return a string
	def intToRoman(self, num):
		dict = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V",
			6:"VI", 7:"VII", 8:"VIII", 9:"IX", 
			10:"X", 20:"XX", 30:"XXX", 40:"XL", 50:"L",
			60:"LX", 70:"LXX", 80:"LXXX", 90:"XC",
			100:"C", 200:"CC", 300:"CCC", 400:"CD", 500:"D",
			600:"DC", 700:"DCC", 800:"DCCC", 900:"CM",
			1000:"M", 2000:"MM", 3000:"MMM"			
			}

		thousand = num / 1000
		hundred  = (num - thousand * 1000) /100
		ten  = (num - thousand * 1000 - hundred * 100) /10
		digit  = num %  10
		A = []
		if thousand != 0:
			A.append(dict[thousand*1000])
		if hundred != 0:
			A.append(dict[hundred*100])
		if ten != 0:
			A.append(dict[ten*10])
		if digit != 0:
			A.append(dict[digit])
		return "".join(A)
        