#Each test case begins with an integer . In the next line,  integers follow representing the elements of array .
from sys import stdin
import itertools
def nonContinuousSum(x):
	gMax = x[0]
	for i in range(1,len(x)):
		if(x[i] < 0 and x[i] > gMax):
			gMax = x[i]
		elif(x[i] < 0 and x[i] < gMax):
			continue
		else:
			gMax = max(gMax ,(gMax + x[i] ))
			#print(sum)
	return gMax 
def continuousSum(x):
	curMax = x[0]
	gMax = x[0]
	for i in range(1,len(x)):
		curMax = max(x[i], curMax + x[i])
		gMax = max(curMax, gMax)
		#print(gMax)
	return gMax
	
data = stdin.readline().rstrip()
T = int(data)
if(T<1 or T>10):
	raise SystemExit
for i in range(T):
	firstarray =[]
	count = stdin.readline().rstrip()
	N = int(count)
	if(N < 1 or N > pow(10,5)):
		raise SystemExit
	temp1 = stdin.readline().rstrip().split(' ')
	for i in range(len(temp1)):
		if(int(temp1[i]) < -pow(10,4) or int(temp1[i])> pow(10,4) ):
			raise SystemExit
		else:
			firstarray.append(int(temp1[i]))
	print(continuousSum(firstarray) ,nonContinuousSum(firstarray) )
	continue
