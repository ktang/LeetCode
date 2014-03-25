'''
Gas Station Total Accepted: 8759 Total Submissions: 36746
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
 You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.

class Solution:
	# @param gas, a list of integers
	# @param cost, a list of integers
	# @return an integer
	def canCompleteCircuit(self, gas, cost):
		def sum(L):
			n = 0
			for i in L:
				n += i
			return n;
		
		print len(gas)
		print range(0, len(gas))
		diff = []# diff = gas - cost
		for i in range(0, len(gas)):
			print i
			diff.append(gas[i] - cost[i])
		
		print gas
		print cost
		print diff
		
		mysum = sum(diff)
		if mysum < 0:
			return -1
		
		index = 0
		length = len(diff)
		for index in range(0, length):
			if diff[index] <= 0:
				continue
			curr_sum = 0
			start_i = index
			while True:
				curr_sum += diff[start_i]
				if curr_sum < 0:
					break
				start_i += 1
				if start_i == index:
					return index
				if start_i == length:
					start_i = 0
		return -1

'''

class Solution:
	# @param gas, a list of integers
	# @param cost, a list of integers
	# @return an integer
	def canCompleteCircuit(self, gas, cost):
		def sum(L):
			n = 0
			for i in L:
				n += i
			return n;
		
		def startSearch(diff, index):
			start_i = index
			curr_sum = 0
			length = len(diff)
			while True:
				curr_sum += diff[start_i]
				if curr_sum < 0:
					return -1
				start_i += 1
				if start_i == index:
					return index
				if start_i == length:
					start_i = 0
		
		diff = []# diff = gas - cost
		for i in range(0, len(gas)):
			diff.append(gas[i] - cost[i])

		mysum = sum(diff)
		if mysum < 0:
			return -1
		
		# only one station situation	
		if len(diff) == 1 and mysum >= 0:
			return 0
		
		index = 0
		length = len(diff)
		lastNeg = diff[-1] <= 0
		while index < length:
			if diff[index] <= 0:
				lastNeg = True
				index += 1
				continue
			if lastNeg:
				res = startSearch(diff, index)
				if res >= 0:
					return res
			lastNeg = False
			index += 1
			
		return -1


gas = [2,4,7]
cost = [3,5,5]

a =Solution()
print a.canCompleteCircuit(gas, cost)