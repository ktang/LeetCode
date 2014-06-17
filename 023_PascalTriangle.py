'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        res = [[1],[1,1]]
        lastRes=[1,1]
        for i in range(3,numRows+1):
            currRes=[]
            for j in range(1,i+1):
                if j == 1:
                    currRes.append(1)
                elif j == i:
                    currRes.append(1)
                else:
                    currRes.append( lastRes[j-2]+lastRes[j-1] )
            res.append(currRes)
            lastRes=currRes
        return res
'''

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
      #  if numRows==0:
       #     return []
        
        res = []
        lastRes=[]
        for i in range(1,numRows+1):
            currRes=[]
            for j in range(1,i+1):
                if j == 1:
                    currRes.append(1)
                elif j == i:
                    currRes.append(1)
                else:
                    currRes.append( lastRes[j-2]+lastRes[j-1] )
            res.append(currRes)
            lastRes=currRes
        return res

#res = [[1],[1,1]]
#print res
a =Solution()
print a.generate(0)
print a.generate(1)
print a.generate(2)
print a.generate(3)
print a.generate(4)
print a.generate(5)
print a.generate(9)